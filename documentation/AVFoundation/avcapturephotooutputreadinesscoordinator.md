# AVCapturePhotoOutputReadinessCoordinator

**Framework**: AVFoundation  
**Kind**: class

An object that monitors changes to a photo output’s capture readiness.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCapturePhotoOutputReadinessCoordinator
```

#### Overview

Use this object to coordinate user interface updates on the main queue with a [`AVCapturePhotoOutput`](avcapturephotooutput.md) that runs on a background queue. Adopt the [`AVCapturePhotoOutputReadinessCoordinatorDelegate`](avcapturephotooutputreadinesscoordinatordelegate.md) protocol in your app and set its implementation as the coordinator’s delegate object to receive callbacks as the associated photo output’s [`captureReadiness`](avcapturephotooutput/capturereadiness-swift.property.md) state changes.

You can track additional capture requests with this object by calling its [`startTrackingCaptureRequest(using:)`](avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:).md) method. You can use it to synchronously update shutter button availability and appearance and on the main thread while calling the photo output’s [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method asynchronously on a background queue.

## Topics

### Creating a coordinator
- [init(photoOutput: AVCapturePhotoOutput)](avcapturephotooutputreadinesscoordinator/init(photooutput:).md)
  Creates an object that helps coordinate user interface changes with a photo output that runs on a background queue.
### Setting the delegate object
- [var delegate: (any AVCapturePhotoOutputReadinessCoordinatorDelegate)?](avcapturephotooutputreadinesscoordinator/delegate.md)
  The coordinator’s delegate object.
### Performing tracking requests
- [func startTrackingCaptureRequest(using: AVCapturePhotoSettings)](avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using:).md)
  Tracks a capture request that uses the specified photo settings.
- [func stopTrackingCaptureRequest(using: Int64)](avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest(using:).md)
  Stop tracking the capture request represented by the specified photo setting’s unique identifier.
### Determining readiness for capture
- [var captureReadiness: AVCapturePhotoOutput.CaptureReadiness](avcapturephotooutputreadinesscoordinator/capturereadiness.md)
  A value that indicates whether the coordinator’s photo output is ready to respond to new capture requests in a timely manner.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Capturing consistent color images](capturing-consistent-color-images.md)
  Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing Still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](avcapturephoto.md)
  A container for image data from a photo capture output.
- [class AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [class AVCapturePhotoOutput](avcapturephotooutput.md)
  A capture output for still image, Live Photos, and other photography workflows.
- [protocol AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md)
  Methods for monitoring progress and receiving results from a photo capture output.
- [protocol AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md)
  A delegate protocol to receive updates about a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator)*