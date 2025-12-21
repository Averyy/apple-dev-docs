# AVCapturePhotoCaptureDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for monitoring progress and receiving results from a photo capture output.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
protocol AVCapturePhotoCaptureDelegate : NSObjectProtocol
```

## Mentions

- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)
- [Saving captured photos](saving-captured-photos.md)

#### Overview

You implement methods in the [`AVCapturePhotoCaptureDelegate`](avcapturephotocapturedelegate.md) protocol to be notified of progress and results when capturing photos with the [`AVCapturePhotoOutput`](avcapturephotooutput.md) class.

To capture a photo, you pass an object implementing this protocol to the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, along with a settings object that describes the capture to be performed. As the capture proceeds, the photo output calls several of the methods in this protocol on your delegate object, providing information about the capture’s progress and delivering the resulting photos.

Which delegate methods the photo output calls depends on the photo settings you initiate capture with. All methods in this protocol are optional at compile time, but at run time your delegate object must respond to certain methods depending on your photo settings:

- If you request a still photo capture (by specifying image formats or file types), your delegate either must implement the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method, or must implement methods listed in `Receiving Capture Results (Deprecated)` corresponding to whether you request capture in RAW format, processed format, or both.
- If you request Live Photo capture (by setting the [`livePhotoMovieFileURL`](avcapturephotosettings/livephotomoviefileurl.md) property to a non-`nil` value), your delegate must implement the [`photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md) method.

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your delegate does not meet these requirements, that method raises an exception.

You must use a unique [`AVCapturePhotoSettings`](avcapturephotosettings.md) object for each capture request. When the photo output calls your delegate methods, it provides an [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object whose [`uniqueID`](avcapturephotosettings/uniqueid.md) property matches that of the photo settings you requested capture with. When making multiple captures, use this unique ID to determine which delegate method calls correspond to which requests.

The photo output always calls each method listed in Monitoring Capture Progress exactly once for each capture request. For methods listed in Receiving Capture Results, you may receive a call more than once, or not at all, depending on your photo settings. See the description of each method for details.

## Topics

### Monitoring capture progress
- [func photoOutput(AVCapturePhotoOutput, willBeginCaptureFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md)
  Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [func photoOutput(AVCapturePhotoOutput, willCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:).md)
  Notifies the delegate that photo capture is about to occur.
- [func photoOutput(AVCapturePhotoOutput, didCapturePhotoFor: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:).md)
  Notifies the delegate that the photo has been taken.
- [func photoOutput(AVCapturePhotoOutput, didFinishCaptureFor: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:).md)
  Notifies the delegate that the capture process is complete.
### Receiving capture results
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: AVCapturePhoto, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md)
  Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishRecordingLivePhotoMovieForEventualFileAt: URL, resolvedSettings: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:didfinishrecordinglivephotomovieforeventualfileat:resolvedsettings:).md)
  Notifies the delegate that the movie content of a Live Photo has finished recording.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingLivePhotoToMovieFileAt: URL, duration: CMTime, photoDisplayTime: CMTime, resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md)
  Provides the delegate the movie file URL resulting from a Live Photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishCapturingDeferredPhotoProxy: AVCaptureDeferredPhotoProxy?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:).md)
  Tells the delegate when the system finishes capturing the photo proxy.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:).md)
  Provides the delegate a captured image in a processed format (such as JPEG).
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingRawPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md)
  Provides the delegate a captured image in RAW format.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Capturing consistent color images](capturing-consistent-color-images.md)
  Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
  Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](avcapturephoto.md)
  A container for image data from a photo capture output.
- [class AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [class AVCapturePhotoOutput](avcapturephotooutput.md)
  A capture output for still image, Live Photos, and other photography workflows.
- [class AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md)
  An object that monitors changes to a photo output’s capture readiness.
- [protocol AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md)
  A delegate protocol to receive updates about a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate)*