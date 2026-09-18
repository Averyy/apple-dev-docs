# Registering a camera capture accessory on iPhone Duo

**Framework**: AVFoundation

Provide content to the person in front of the camera by pairing it with your capture interface.

#### Overview

Consider an app that records someone reading from a script. The person holding the device sees the capture interface, and the person in front of the camera sees nothing. They look away from the lens to read, or they memorize the script and lose the take. On iPhone Duo, an outer display faces the same way as the camera, so the app presents the script to the person who needs to read from it.

![An illustration of the iPhone Duo, fully open and seen from the back. The rear cameras sit on one panel, and the outer display fills the other, facing the same direction as those cameras. The display shows several lines of a script for the person in front of the camera to read.](/images/com.apple.avfoundation/camera-capture-accessory-script@2x.png)

Your app declares the content as a [`UISceneAccessory`](https://developer.apple.com/documentation/uikit/uisceneaccessory) and attaches it to the view that shows your capture interface. The system decides when and where to present it. Presentation happens while your app is in the foreground with an active capture session, while the capture interface runs on the inner display. Because the decision belongs to the system, treat accessory content as an enhancement.

#### Decide What to Show on the Outer Display

Decide what the person in front of the camera needs to see while recording. For example, your app can scroll a script at a readable pace, count down before recording starts, or show how much of the subject the camera sees.

Consider the following before you design the content:

- Let the system choose where the content appears. Your app declares a kind of content and passes no display, capture session, or camera reference. The system finds the active capture session itself.
- Keep any interaction minimal. Anything your app shows on the outer display is an enhancement. The display accepts touch, which suits a single capture task such as tapping a preview to focus, rather than a second interface. Keep all essential controls in your capture interface, because the system can withdraw accessory content at any time.
- Expect the content to appear and disappear on its own. The system decides when to present the content, based on conditions outside your app.

Design your capture interface so it works when no outer display exists, and when the system presents nothing there. Accessory content enhances your app, and never carries a task your app can’t complete without it.

#### Register Content on Your Capture Interface

To scope content to the camera, register the accessory on the same view that shows your capture interface. The system presents your content only while that interface is onscreen, and stops when someone navigates away. Registration returns an object that reports whether the system can present the content. Later sections use that object to respond to availability and to turn the content off.

**SwiftUI**:

Add the [`sceneAccessory(content:)`](https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:)) modifier to the view that shows your capture interface, and declare a [`CameraCaptureAccessory`](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory) inside it:

```swift
struct CameraView: View {

    @State private var script = ScriptModel()

    var body: some View {
        CameraPreview()
            .sceneAccessory {
                CameraCaptureAccessory {
                    ScriptView(model: script)
                }
            }
    }
}
```

**UIKit**:

Create an accessory with the [`cameraCapture(sceneConfiguration:userInfo:)`](https://developer.apple.com/documentation/uikit/uisceneaccessory/cameracapture(sceneconfiguration:userinfo:)) factory method, and pass it to [`registerSceneAccessory(_:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/registersceneaccessory(_:)) on the view controller that shows your capture interface:

```swift
class CameraViewController: UIViewController {

    private let script = ScriptModel()
    private var registration: UISceneAccessoryRegistration?

    override func viewDidLoad() {
        super.viewDidLoad()

        let configuration = UISceneConfiguration()
        configuration.delegateClass = ScriptSceneDelegate.self

        let accessory = UISceneAccessory.cameraCapture(sceneConfiguration: configuration,
                                                       userInfo: script)
        registration = registerSceneAccessory(accessory)
    }
}
```

Hold a strong reference to the [`UISceneAccessoryRegistration`](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration) that registering returns. Your app reads and sets its properties to track availability and to turn the content off. Call [`unregisterSceneAccessory(_:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/unregistersceneaccessory(_:)) when your app stops offering the content, rather than hiding it.

The system assigns the session role for the accessory’s scene, and your app never sets it. Unlike ordinary window scenes, accessory scenes have no project-level configuration, so a scene manifest entry for one has no effect. If your scene delegate handles several kinds of scene, compare the session role against [`windowCameraCaptureAccessory`](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowcameracaptureaccessory) to identify this one.

#### Share State with Your Accessory Content

Your capture interface and your accessory content belong to the same capture session, so both need the same state. Rather than sending updates to your accessory content, give it the object your app already uses, and let each side read what it needs. A control the subject taps on the outer display then changes what the person holding the device sees, with no message passing in between.

**SwiftUI**:

The content closure captures the state around it, and makes an observable model visible inside the accessory. The following view scrolls a script on the outer display, and its controls change the same model the capture interface reads:

```swift
struct ScriptView: View {

    let model: ScriptModel

    var body: some View {
        VStack {
            ScrollingText(text: model.text, position: model.position)

            HStack {
                Button(model.isScrolling ? "Pause" : "Play") {
                    model.isScrolling.toggle()
                }
                Slider(value: $model.speed, in: 0.5...2.0)
            }
        }
    }
}
```

**UIKit**:

Pass the object to the accessory as its `userInfo` value, as the previous section shows, and read it back when the accessory’s scene connects:

```swift
class ScriptSceneDelegate: NSObject, UIWindowSceneDelegate {

    var window: UIWindow?

    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {
        guard let windowScene = scene as? UIWindowScene,
              let script = connectionOptions.sceneAccessoryUserInfo as? ScriptModel else { return }

        let window = UIWindow(windowScene: windowScene)
        window.rootViewController = ScriptViewController(model: script)
        window.makeKeyAndVisible()
        self.window = window
    }
}
```

Keep a strong reference to the object you pass. The accessory identifies the object for the scene, and isn’t a place to store it.

#### Respond to Changes in Availability

Availability tells you whether the system can present your content, and only the system sets it. Turning the content on and off is your app’s decision, and the registration keeps the two separate. When the system can’t present anything, hide the outer display controls.

**SwiftUI**:

Add [`onAvailabilityChange(perform:)`](https://developer.apple.com/documentation/swiftui/sceneaccessorycontent/onavailabilitychange(perform:)) to your accessory content:

```swift
CameraCaptureAccessory {
    ScriptView(model: script)
}
.onAvailabilityChange { isAvailable in
    showsScriptControls = isAvailable
}
```

**UIKit**:

Read [`isAvailable`](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isavailable) where you update your interface. Availability supports observation, so reading it in [`updateProperties()`](https://developer.apple.com/documentation/uikit/uiviewcontroller/updateproperties()) keeps your controls current without a notification:

```swift
override func updateProperties() {
    super.updateProperties()

    scriptControls.isHidden = !(registration?.isAvailable ?? false)
}
```

Availability changes for reasons your app doesn’t cause. The system presents the top-most registration of a kind. Navigating to a view that registers its own content makes the previous one unavailable, and going back restores it. Availability also follows the device and the capture session. Content goes away when capture stops, when your app leaves the foreground, or when someone folds the device closed.

When the system can’t present anything, the registration stays inactive and availability stays false, which means one code path works everywhere. Accessories of different kinds never compete. An app that shows slides on a connected display can present capture content on the outer display at the same time.

#### Let People Turn the Content Off

Rather than unregistering the accessory, give people a control in your capture interface that turns the content off. Turning the content off says nothing about whether the system can present anything.

**SwiftUI**:

Pass a binding to the accessory, and bind it to a control in your interface:

```swift
CameraCaptureAccessory(isEnabled: $isScriptEnabled) {
    ScriptView(model: script)
}
```

**UIKit**:

Set [`isEnabled`](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isenabled) on the registration:

```swift
registration?.isEnabled = isScriptEnabled
```

Accessory content is on by default. Turning it off dismisses the content, and the views come and go the way your main scene’s do. Keep any state that has to persist in your model rather than in the view that presents it.

#### Test Your Accessory Content on Device

Create your app’s accessory content from ordinary views, so you can check its layout in previews or in Simulator, and confirm that it reads the same state as your capture interface.

Because Simulator doesn’t have a camera, always test anything that depends on camera capture on a device before you ship your app. The system presents content only when the device is open, your app is in the foreground, and a capture session is running.

## See Also

- [Setting up a capture session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Building a responsive camera app that launches quickly](building-a-responsive-camera-app-that-launches-quickly.md)
  Show a camera preview sooner by deferring capture output setup and postponing noncritical interface elements.
- [Capturing Cinematic video](capturing-cinematic-video.md)
  Capture video with an adjustable depth of field and focus points.
- [Supporting Center Stage front camera in your iOS app](supporting-center-stage-front-camera-in-your-ios-app.md)
  Enable Center Stage for photos and videos on the iPhone front camera.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md)
  Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: detecting barcodes and faces](avcambarcode-detecting-barcodes-and-faces.md)
  Identify machine readable codes or faces by using the camera.
- [class AVCaptureSession](avcapturesession.md)
  An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [class AVCaptureMultiCamSession](avcapturemulticamsession.md)
  A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [class AVCaptureInput](avcaptureinput.md)
  An abstract superclass for objects that provide input data to a capture session.
- [class AVCaptureOutput](avcaptureoutput.md)
  An abstract superclass for objects that provide media output destinations for a capture session.
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/registering-a-camera-capture-accessory-on-iphone-duo)*