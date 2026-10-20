# AVCapturePhotoOutputReadinessCoordinatorDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A delegate protocol to receive updates about a photo output’s capture readiness.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
protocol AVCapturePhotoOutputReadinessCoordinatorDelegate : NSObjectProtocol
```

```objc
@protocol AVCapturePhotoOutputReadinessCoordinatorDelegate <NSObject>
```

## Topics

### Monitoring capture readiness
- [func readinessCoordinator(AVCapturePhotoOutputReadinessCoordinator, captureReadinessDidChange: AVCapturePhotoOutput.CaptureReadiness)](./avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator%28_,capturereadinessdidchange%29.md)
  Tells the delegate that the capture readiness state of a photo output changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Photo capture
- [Capturing consistent color images](./capturing-consistent-color-images.md)
  Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](./capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](./capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](./avcapturephoto.md)
  A container for image data from a photo capture output.
- [class AVCaptureDeferredPhotoProxy](./avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [class AVCapturePhotoOutput](./avcapturephotooutput.md)
  A capture output for still image, Live Photos, and other photography workflows.
- [protocol AVCapturePhotoCaptureDelegate](./avcapturephotocapturedelegate.md)
  Methods for monitoring progress and receiving results from a photo capture output.
- [class AVCapturePhotoOutputReadinessCoordinator](./avcapturephotooutputreadinesscoordinator.md)
  An object that monitors changes to a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](./avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate)*