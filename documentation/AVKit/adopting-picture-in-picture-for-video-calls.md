# Adopting Picture in Picture for video calls

**Framework**: AVKit  
**Role**: Article

Add multitasking capability to your video-call apps by using Picture in Picture (PiP).

## Overview

Use PiP in your video-call apps so users can multitask with other apps while on video calls. When a user enables PiP, your app scales down to a corner of the screen, so they can see the Home Screen and interact with other apps. In iOS 15 and later, [AVKit](./AVKit.md) provides PiP support for video-calling apps, which enables you to deliver a familiar video-calling experience that behaves like FaceTime.

> ❗ **Important**:  In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [`isMultitaskingCameraAccessEnabled`](../AVFoundation/avcapturesession/ismultitaskingcameraaccessenabled.md) property. Apps that have a deployment target earlier than iOS 16 require the [`com.apple.developer.avfoundation.multitasking-camera-access`](../BundleResources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement to use the camera in PiP mode.

### Create a source view

Providing PiP support begins by choosing a source view to display inside the video-call view controller. You need to add a `UIView` to `AVPictureInPictureVideoCallViewController`, so use [`AVCaptureVideoPreviewLayer`](../AVFoundation/avcapturevideopreviewlayer.md) or [`AVSampleBufferDisplayLayer`](../AVFoundation/avsamplebufferdisplaylayer.md) depending on your need. In iOS 18 and later, you may also use [`MTKView`](../MetalKit/mtkview.md) as your source view. Video-calling apps need to display the remote view, so use [`AVSampleBufferDisplayLayer`](../AVFoundation/avsamplebufferdisplaylayer.md) to do so.

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

### Create a video-call controller

To display your source view, create a [`AVPictureInPictureVideoCallViewController`](./avpictureinpicturevideocallviewcontroller.md) and add your source as a subview.

```swift
let pipVideoCallViewController = AVPictureInPictureVideoCallViewController()
pipVideoCallViewController.preferredContentSize = CGSize(width: 1080, height: 1920)
pipVideoCallViewController.view.addSubview(sampleBufferVideoCallView)
```

Use [`isPictureInPictureSupported()`](./avpictureinpicturecontroller/ispictureinpicturesupported%28%29.md) to determine whether the current device supports PiP playback. If PiP isn’t supported on the current device, attempting to initialize a PiP controller returns `nil`.

### Create a PiP controller using a content source

Before you create an [`AVPictureInPictureController`](./avpictureinpicturecontroller.md), you need to create an [`AVPictureInPictureController.ContentSource`](./avpictureinpicturecontroller/contentsource-swift.class.md) that represents the source of the content the system displays. A content source requires a video-call view controller, and a source view that contains the content you associate with the video call.

```swift
let pipContentSource = AVPictureInPictureController.ContentSource(
                            activeVideoCallSourceView: videoCallViewSourceView, 
                            contentViewController: pipVideoCallViewController)
```

> ❗ **Important**:  Avoid unintentionally starting PiP by setting the content source on your PiP controller to `nil` or by releasing your PiP controller, when the active call ends.

After creating a content source, use it to initialize [`AVPictureInPictureController`](./avpictureinpicturecontroller.md). By default, PiP starts when a user moves to the background if your source view is full-screen, or you set [`canStartPictureInPictureAutomaticallyFromInline`](./avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.md) to `true`. If your app is in the foreground, you can start PiP by calling [`startPictureInPicture()`](./avpictureinpicturecontroller/startpictureinpicture%28%29.md).

```swift
let pipController = AVPictureInPictureController(contentSource: pipContentSource)
pipController.canStartPictureInPictureAutomaticallyFromInline = true
pipController.delegate = self
```

The system uses the source view to determine the source frame for the PiP animation, and the restore target for either when the user returns to the app or PiP stops.

> **Note**:  The PiP window doesn’t receive touch events when you use [`AVPictureInPictureVideoCallViewController`](./avpictureinpicturevideocallviewcontroller.md), so you can’t customize the window’s user interface by adding buttons.

### Observe PiP life cycle events

When you use PiP, you respond to life-cycle events by observing [`AVPictureInPictureControllerDelegate`](./avpictureinpicturecontrollerdelegate.md). This allows you to handle your app’s user interface based on the PiP state, along with observing for potential errors.

The system interrupts your capture session when the system or user stashes PiP, so observe [`wasInterruptedNotification`](../AVFoundation/avcapturesession/wasinterruptednotification.md) for [`AVCaptureSession.InterruptionReason.videoDeviceNotAvailableInBackground`](../AVFoundation/avcapturesession/interruptionreason/videodevicenotavailableinbackground.md) to handle the interruption.

When your app is in PiP mode, it can’t assume control of the camera. For example, Camera.app assumes control of the camera when it’s opened, and the system returns camera control when Camera.app finishes with it. You observe [`wasInterruptedNotification`](../AVFoundation/avcapturesession/wasinterruptednotification.md) for [`AVCaptureSession.InterruptionReason.videoDeviceInUseByAnotherClient`](../AVFoundation/avcapturesession/interruptionreason/videodeviceinusebyanotherclient.md) to handle the interruption.

## See Also

### Picture in Picture
- [Adopting Picture in Picture in a standard player](./adopting-picture-in-picture-in-a-standard-player.md)
  Add Picture in Picture (PiP) playback to your app using a player view controller.
- [Adopting Picture in Picture in a custom player](./adopting-picture-in-picture-in-a-custom-player.md)
  Add controls to your custom player user interface to invoke Picture in Picture (PiP) playback.
- [Adopting Picture in Picture playback in tvOS](./adopting-picture-in-picture-playback-in-tvos.md)
  Add advanced multitasking capabilities to your video apps by using Picture in Picture playback in tvOS.
- [class AVPictureInPictureController](./avpictureinpicturecontroller.md)
  A controller that responds to user-initiated Picture in Picture playback of video in a floating, resizable window.
- [protocol AVPictureInPictureControllerDelegate](./avpictureinpicturecontrollerdelegate.md)
  A protocol to adopt to respond to Picture in Picture events.
- [protocol AVPictureInPictureSampleBufferPlaybackDelegate](./avpictureinpicturesamplebufferplaybackdelegate.md)
  A protocol for controlling playback from a sample buffer display layer in Picture in Picture.
- [class AVPictureInPictureVideoCallViewController](./avpictureinpicturevideocallviewcontroller.md)
  A view controller that presents content from a video call in Picture in Picture.
- [protocol AVPlayerViewPictureInPictureDelegate](./avplayerviewpictureinpicturedelegate.md)
  A protocol that defines the methods to implement to respond to Picture in Picture playback events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-for-video-calls)*