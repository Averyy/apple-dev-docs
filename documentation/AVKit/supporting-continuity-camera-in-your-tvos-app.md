# Supporting Continuity Camera in your tvOS app

**Framework**: AVKit

Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.

**Availability**:
- tvOS 17.0+
- Xcode 15.3+

#### Overview

Continuity Camera brings the power of the cameras and microphones from an iOS or iPadOS device to Apple TV, including advanced features like Center Stage and Portrait mode.

This sample project provides an example implementation that accesses a camera and microphone from a nearby iPhone or iPad in an Apple TV app. It builds on a similar sample, [`Supporting Continuity Camera in your macOS app`](https://developer.apple.com/documentation/avfoundation/supporting-continuity-camera-in-your-macos-app), and shares some of its functionality, including automatic camera selection and observing the state of video effects. The following sections focus on the aspects specific to tvOS.

> **Note**: This sample code project is associated with WWDC23 session 10256: [`Discover Continuity Camera on tvOS`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10256).

##### Configure the Sample Code Project

To run this sample app, you need the following:

- An Apple TV 4k (2nd generation) or later with tvOS 17 or later.
- An iPhone or iPad with iOS 17 or iPadOS 17, respectively, or later.

You need to run this sample code project on physical devices, because Simulator doesn’t include the components to support cameras.

Continuity Camera works with all iPhone and iPad models that support video effects in Control Center. You need to sign in with an Apple ID that uses two-factor authentication for the Apple TV and the device with a camera. You can use a separate Apple ID for each device or the same Apple ID for both.

The first time you run the app on an Apple TV, the system prompts you for permission to access to the camera and microphone. The app needs these permissions to function correctly.

##### Present the Continuity Device Picker

When the app launches, it immediately presents a continuity device picker by calling the [`continuityDevicePicker(isPresented:onDidConnect:)`](https://developer.apple.com/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:)) modifier in its SwiftUI implementation.

```swift
.continuityDevicePicker(isPresented: $showContinuityDevicePicker,
                        onDidConnect: handleNewConnectionForDevice)
.task {
    // Shows the picker when app has no continuity device at launch.
    if !captureManager.activateDefaultContinuityCameraDevice() {
        showContinuityDevicePicker = true
    }
```

The picker only appears if the `isPresented` parameter — which is a Boolean [`Binding`](https://developer.apple.com/documentation/swiftui/binding) — is `true`. The picker calls the closure the app passes to the `onDidConnect` parameter when a person selects a device and the system successfully connects to it.

```swift
func handleNewConnectionForDevice(_ device: AVContinuityDevice?) {
    guard let device else {
        print("The Continuity Device Picker didn't connect a device.")
        return
    }

    guard let firstCamera = device.videoDevices.first else {
        print("The Continuity Device Picker doesn't have any cameras.")
        return
    }

    captureManager.setActiveVideoInput(firstCamera,
                                       isUserPreferredCamera: true)
}
```

The handling closure’s [`AVContinuityDevice`](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice) parameter represents the device that a person selects on their Apple TV. Each continuity device has a [`videoDevices`](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice/videodevices) property, which is an array of [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) instances.

The app’s `handleNewConnectionForDevice(_:)` method is a minimal implementation that selects the first video device in the array. Apps typically compare all the video device elements and select one that’s appropriate for their needs.

> **Note**: [`UIKit`](https://developer.apple.com/documentation/uikit) based apps can create a continuity device picker by creating an [`AVContinuityDevicePickerViewController`](avcontinuitydevicepickerviewcontroller.md) instance.

##### Connect a Video Device to a Capture Session

The app’s `CaptureManager` class creates and maintains an [`AVCaptureSession`](https://developer.apple.com/documentation/avfoundation/avcapturesession) instance for the app’s lifetime. The capture manager’s `setActiveVideoInput(_:)` method creates an [`AVCaptureDeviceInput`](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput) instance from the video device, and then tests to see whether it’s an acceptable input for the capture session.

```swift
let name = camera.localizedName
print("Setting video input to: \(name).")

// Creates a video input with the camera.
guard let videoInput = try? AVCaptureDeviceInput(device: camera) else {
    print("Couldn't make an input from: \(name).")
    return false
}

// Checks whether the capture session accepts the new camera as an input.
guard session.canAddInput(videoInput) else {
    print("Capture session rejected '\(name)' as an input.")
    return false
}

// Adds the new camera input to the capture session.
activeInput = videoInput
```

If the new device is an acceptable input, the method assigns it to the app’s `activeInput` property. The property updates the capture session with its `willSet` and `didSet` property observers.

```swift
internal var activeInput: AVCaptureDeviceInput? {
    willSet {
        if let oldInput = activeInput {
            session.removeInput(oldInput)
        }
    }
    didSet {
        if let newInput = activeInput {
            session.addInput(newInput)
        }
        isActive = (activeInput != nil)
    }
}
```

The `willSet` observer removes the capture session’s current input, if applicable. The `didSet` observer adds the new input to the capture session. The `didSet` observer also updates the `isActive` Boolean property, which can cause the app to change its behavior and UI.

##### Register for Capture Device Updates

The app receives various updates related to its capture device by registering with [`NotificationCenter`](https://developer.apple.com/documentation/foundation/notificationcenter) and with key-value observation (KVO). See [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/swift/using-key-value-observing-in-swift) and [`NSKeyValueObserving`](https://developer.apple.com/documentation/objectivec/nskeyvalueobserving) for more information.

The app specifically registers for the following events:

- A specific video effect, such as Center Stage, changes its active state.
- The system changes the capture device it prefers.
- The active capture device disconnects from the system.

> **Note**: People can enable video effects in Control Center on Apple TV.

The sample’s implementation that monitors the video effects and system changes is similar to the macOS equivalent of this sample, [`Supporting Continuity Camera in your macOS app`](https://developer.apple.com/documentation/avfoundation/supporting-continuity-camera-in-your-macos-app). The sample also monitors Notification Center events related to the camera. The app’s capture manager responds when a capture device disconnects by registering with Notification Center for the [`wasConnectedNotification`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/wasconnectednotification) event.

```swift
func observeCamera(_ camera: AVCaptureDevice) {
    // Tells the observer to watch the new camera's properties.
    videoEffectsObvserver.observeCamera(camera)

    // Tells the notification observer to monitor camera-related events.
    notificationObserver.observeCamera(camera,
                                       with: notification(_:for:))
}
```

The app’s `CaptureDeviceNotificationObserver` structure listens for the these events on behalf of the capture manager and calls the manager’s `notification(_:for:)` method for each event it gets from Notification Center.

##### Configure the Audio Engine with an Audio Input Device

At launch, the app creates an `AudioCapturer` instance, which checks for audio inputs (microphones). It does this by inspecting the [`availableInputs`](https://developer.apple.com/documentation/avfaudio/avaudiosession/availableinputs) property of the [`AVAudioSession`](https://developer.apple.com/documentation/avfaudio/avaudiosession) type’s shared instance, and then monitoring the property for updates.

The app monitors for new microphones — similar to how the app’s capture manager monitors for new cameras — by observing the [`isInputAvailable`](https://developer.apple.com/documentation/avfaudio/avaudiosession/isinputavailable) property of the `AVAudioSession` type’s shared instance.

```swift
private static let inputAvailableKeyPath = "isInputAvailable"

func registerForInputAvailabilityUpdates(on session: AVAudioSession) {
    session.addObserver(self,
                        forKeyPath: Self.inputAvailableKeyPath,
                        options: [.new],
                        context: nil)
}
```

When the app has access to a microphone, it configures an [`AVAudioEngine`](https://developer.apple.com/documentation/avfaudio/avaudioengine) instance in the audio capturer’s `setupAndStartAudioSession()` method.

```swift
func setupAndStartAudioSession() {
    configureAudioOutput()
    enableVoiceProcessing(true)
    configureAudioSessionForVoiceChat()
    startAudioEngine()
}
```

The method configures the audio engine for a conference call scenario when the app gains access to a microphone — at launch or later — with the following steps:

1. Configures the audio engine to produce sound from the system’s first audio output.
2. Enables voice processing on the audio engine’s input node.
3. Configures the audio engine for conversational audio.
4. Starts the audio engine.

##### Configure the Audio Engine for a Call

The third step is important for conferencing apps that use Voice over IP (VoIP). The `configureAudioSessionForVoiceChat` method configures the audio session by passing the [`voiceChat`](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.struct/voicechat) mode to the audio session’s [`setCategory(_:)`](https://developer.apple.com/documentation/avfaudio/avaudiosession/setcategory(_:)) method.

```swift
try avAudioSession.setCategory(.playAndRecord,
                               mode: .voiceChat,
                               options: [])
```

The app gains access to additional audio features and microphone modes, including automatic gain correction, voice processing, and muting, by configuring the audio session for VoIP.

The app’s audio interface has a button that lets a person temporarily disable microphone processing, including echo cancellation, by bypassing the audio engine’s voice processing. Each time a person toggles the button, the app calls audio capturer’s `bypassVoiceProcessing(_:)` method.

```swift
public func bypassVoiceProcessing(_ bypass: Bool) {
    // If true, temporarily disables echo cancelation.
    avAudioEngine.inputNode.isVoiceProcessingBypassed = bypass

    DispatchQueue.main.async {
        self.isVoiceProcessingBypassed = bypass
    }

    var message = "Audio engine's voice processing: "
    message += bypass ? "bypassed" : "normal"
    print(message)
}
```

The app can temporarily disable voice processing by setting the [`isVoiceProcessingBypassed`](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/isvoiceprocessingbypassed) property of the audio engine’s [`inputNode`](https://developer.apple.com/documentation/avfaudio/avaudioengine/inputnode) to `true`. This gives the app all the incoming audio from the microphone without any adjustments from the system.

> **Note**: The behavior of the audio engine’s `isVoiceProcessingBypassed` property is similar to [`kAUVoiceIOProperty_BypassVoiceProcessing`](https://developer.apple.com/documentation/audiotoolbox/kauvoiceioproperty_bypassvoiceprocessing). For more information, see [`Audio Unit Voice I/O`](https://developer.apple.com/documentation/audiotoolbox/audio-unit-voice-i-o).

## See Also

- [Customizing the tvOS Playback Experience](customizing-the-tvos-playback-experience.md)
  Adopt the latest features of the redesigned tvOS player user interface to provide a more streamlined way to watch your content.
- [Presenting Navigation Markers](presenting-navigation-markers.md)
  Present navigation markers in the Chapters panel to help users quickly navigate your content.
- [Working with Interstitial Content](working-with-interstitial-content.md)
  Present additional content alongside your main media presentation using HTTP Live Streaming support.
- [Presenting Content Proposals in tvOS](presenting-content-proposals-in-tvos.md)
  Display a preview of an upcoming media item at the conclusion of the currently playing media item.
- [Working with Overlays and Parental Controls in tvOS](working-with-overlays-and-parental-controls-in-tvos.md)
  Add interactive overlays, parental controls, and livestream channel flipping using a player view controller.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVInterstitialTimeRange](avinterstitialtimerange.md)
  A time range in an audiovisual presentation for content with an interstitial designation, such as advertisements or legal notices.
- [class AVNavigationMarkersGroup](avnavigationmarkersgroup.md)
  A set of markers for navigating playback of an audiovisual presentation.
- [class AVContentProposalViewController](avcontentproposalviewcontroller.md)
  A view controller that proposes content to watch next.
- [class AVDisplayManager](avdisplaymanager.md)
  A tvOS management object that controls whether a TV switches modes to match the video’s native mode.
- [class AVContinuityDevicePickerViewController](avcontinuitydevicepickerviewcontroller.md)
  A view controller that provides an interface to a person so they can select and connect a continuity device to the system.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.
- [Third-party casting support](third-party-casting-support.md)
  Provide custom playback controls for third-party casting services and other media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/supporting-continuity-camera-in-your-tvos-app)*