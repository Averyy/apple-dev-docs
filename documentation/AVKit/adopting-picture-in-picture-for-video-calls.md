# Adopting Picture in Picture for video calls

**Framework**: AVKit

Add multitasking capability to your video-call apps by using Picture in Picture (PiP).

#### Overview

Use PiP in your video-call apps so users can multitask with other apps while on video calls. When a user enables PiP, your app scales down to a corner of the screen, so they can see the Home Screen and interact with other apps. In iOS 15 and later, [`AVKit`](AVKit.md) provides PiP support for video-calling apps, which enables you to deliver a familiar video-calling experience that behaves like FaceTime.

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/isMultitaskingCameraAccessEnabled) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.avfoundation.multitasking-camera-access) entitlement to use the camera in PiP mode.

##### Create a Source View

Providing PiP support begins by choosing a source view to display inside the video-call view controller. You need to add a `UIView` to `AVPictureInPictureVideoCallViewController`, so use [`AVCaptureVideoPreviewLayer`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoPreviewLayer) or [`AVSampleBufferDisplayLayer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferDisplayLayer) depending on your need. In iOS 18 and later, you may also use [`MTKView`](https://developer.apple.com/documentation/MetalKit/MTKView) as your source view. Video-calling apps need to display the remote view, so use [`AVSampleBufferDisplayLayer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferDisplayLayer) to do so.

```swift
class SampleBufferVideoCallView: UIView {
    override class var layerClass: AnyClass {
        AVSampleBufferDisplayLayer.self
    }
    
    var sampleBufferDisplayLayer: AVSampleBufferDisplayLayer {
        layer as! AVSampleBufferDisplayLayer
    }
}
```

##### Create a Video Call Controller

To display your source view, create a [`AVPictureInPictureVideoCallViewController`](avpictureinpicturevideocallviewcontroller.md) and add your source as a subview.

```swift
let pipVideoCallViewController = AVPictureInPictureVideoCallViewController()
pipVideoCallViewController.preferredContentSize = CGSize(width: 1080, height: 1920)
pipVideoCallViewController.view.addSubview(sampleBufferVideoCallView)
```

Use [`isPictureInPictureSupported()`](avpictureinpicturecontroller/ispictureinpicturesupported().md) to determine whether the current device supports PiP playback. If PiP isn’t supported on the current device, attempting to initialize a PiP controller returns `nil`.

##### Create a Pip Controller Using a Content Source

Before you create an [`AVPictureInPictureController`](avpictureinpicturecontroller.md), you need to create an [`AVPictureInPictureController.ContentSource`](avpictureinpicturecontroller/contentsource-swift.class.md) that represents the source of the content the system displays. A content source requires a video-call view controller, and a source view that contains the content you associate with the video call.

```swift
let pipContentSource = AVPictureInPictureController.ContentSource(
                            activeVideoCallSourceView: videoCallViewSourceView, 
                            contentViewController: pipVideoCallViewController)
```

> ❗ **Important**:  Avoid unintentionally starting PiP by setting the content source on your PiP controller to `nil` or by releasing your PiP controller, when the active call ends.

After creating a content source, use it to initialize [`AVPictureInPictureController`](avpictureinpicturecontroller.md). By default, PiP starts when a user moves to the background if your source view is full-screen, or you set [`canStartPictureInPictureAutomaticallyFromInline`](avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md) to `true`. If your app is in the foreground, you can start PiP by calling [`startPictureInPicture()`](avpictureinpicturecontroller/startpictureinpicture().md).

```swift
let pipController = AVPictureInPictureController(contentSource: pipContentSource)
pipController.canStartPictureInPictureAutomaticallyFromInline = true
pipController.delegate = self
```

The system uses the source view to determine the source frame for the PiP animation, and the restore target for either when the user returns to the app or PiP stops.

> **Note**:  The PiP window doesn’t receive touch events when you use [`AVPictureInPictureVideoCallViewController`](avpictureinpicturevideocallviewcontroller.md), so you can’t customize the window’s user interface by adding buttons.

##### Observe Pip Life Cycle Events

When you use PiP, you respond to life-cycle events by observing [`AVPictureInPictureControllerDelegate`](avpictureinpicturecontrollerdelegate.md). This allows you to handle your app’s user interface based on the PiP state, along with observing for potential errors.

The system interrupts your capture session when the system or user stashes PiP, so observe [`wasInterruptedNotification`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/wasInterruptedNotification) for [`AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/InterruptionReason/videoDeviceNotAvailableInBackground) to handle the interruption.

When your app is in PiP mode, it can’t assume control of the camera. For example, Camera.app assumes control of the camera when it’s opened, and the system returns camera control when Camera.app finishes with it. You observe [`wasInterruptedNotification`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/wasInterruptedNotification) for [`AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/InterruptionReason/videoDeviceInUseByAnotherClient) to handle the interruption.

## See Also

- [Adopting Picture in Picture Playback in tvOS](adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [Adopting Picture in Picture in a Standard Player](adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a Custom Player](adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Accessing the camera while multitasking on iPad](accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [class AVPictureInPictureController](avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-for-video-calls)*