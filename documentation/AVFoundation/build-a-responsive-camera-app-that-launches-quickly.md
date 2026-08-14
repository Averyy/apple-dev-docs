# Build a responsive camera app that launches quickly

**Framework**: AVFoundation

Build a fast camera launch experience for your iOS and iPadOS apps.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample demonstrates how to use the deferred start API and how to defer UI elements until after preview is running, to optimize a camera app for launch. The FastCameraLaunch sample builds off of AVCam. For more details on AVCam, see [`AVCam: Building a camera app`](avcam-building-a-camera-app.md).

> **Note**: This sample code project is associated with WWDC26 session 303: [`Build a responsive camera app that launches quickly`](https://developer.apple.comhttps://developer.apple.com/wwdc26/303/).

#### Configure the Sample Code Project

The sample app, FastCameraLaunch, requires the following:

- Xcode 27.
- An iOS device running iOS 27 or later.
- FastCameraLaunch doesn’t work in Simulator, because Xcode can’t access the camera,

#### Postpone Non Critical Ui Elements

The app’s UI plays an important role in the camera launch experience. When designing a launch flow, divide the app’s launch into two phases:

- Resources critical for launching and displaying preview
- Resources that can be created after preview is running

In FastCameraLaunch, there are several UI elements: a camera preview, a shutter button, an image well, and a mode picker. The camera preview is the most critical UI element for someone when they launch the app. The image well and the mode picker are not needed prior to preview rendering, so this work needs to wait until after preview has started.

Here’s an example of how to consider postponing elements until after launch:

```swift
@State var camera: CameraModel
var body: some View {
    HStack {
        if camera.status == .running {
            ThumbnailButton(camera: camera)
                // Hide the thumbnail button when a person interacts with capture controls.
                .opacity(camera.prefersMinimizedUI ? 0 : 1)
                .transition(.opacity.animation(.easeIn(duration: 0.3).delay(0.2)))
        }
        Spacer()
        CaptureButton(camera: camera)
        Spacer()
        if camera.status == .running {
            SwitchCameraButton(camera: camera)
                // Hide the camera selection when a person interacts with capture controls.
                .opacity(camera.prefersMinimizedUI ? 0 : 1)
                .transition(.opacity.animation(.easeIn(duration: 0.3).delay(0.2)))
        }
    }
    .foregroundColor(.white)
}
```

#### Opt Into Deferred Start

Initializing [`AVCaptureOutput`](avcaptureoutput.md) objects is expensive, and significantly slows down launch. An app only needs one output initialized in order to render preview. Outputs such as [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) and [`AVCapturePhotoOutput`](avcapturephotooutput.md) are not necessary for preview, while [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md) is essential. To reduce the time spent in `AVCaptureOutput` initialization, use the Deferred Start API.

Each `AVCaptureOutput` and `AVCaptureVideoPreviewLayer` object has an `isDeferredStartEnabled` property. Set this property to `true` to defer an output. To optimize for launch, defer all outputs except the output the app uses to render preview.

There are two ways the app can specify when to run the initializations: Automatic Start and Manual Start.

For apps which that recompile against the iOS 26.0 SDK, the default behavior is to run in automatic mode. The `automaticallyRunsDeferredStart` property is set to `true` when using automatic mode

```swift
// Deferred start.
captureSession.automaticallyRunsDeferredStart = true
photoCapture.output.isDeferredStartEnabled = true
captureSession.setDeferredStartDelegate(deferredStartDelegate, deferredStartDelegateCallbackQueue: sessionQueue)
// Commit the capture session configuration.
captureSession.commitConfiguration()
```

If you want to fine-tune this control in your app, the Deferred Start API offers a manual start option with the `runDeferredStartWhenNeeded` property.

To opt in to this mode, set the `automaticallyRunsDeferredStart` property on [`AVCaptureSession`](avcapturesession.md) to `false`.

Once an app finishes its start-up operations, such as non-critical resource creation, call the `runDeferredStartWhenNeeded` method on the AVCaptureSession to inform the system that now is an good time to run deferred-start initialization

## See Also

- [Setting up a capture session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/build-a-responsive-camera-app-that-launches-quickly)*