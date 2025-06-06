# photoOutput(_:didFinishProcessingPhoto:error:)

**Framework**: AVFoundation  
**Kind**: method

Provides the delegate with the captured image and associated metadata resulting from a photo capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: (any Error)?)
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)
- [Capturing Photos in RAW and Apple ProRAW Formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)
- [Saving Captured Photos](saving-captured-photos.md)
- [Capturing and Saving Live Photos](capturing-and-saving-live-photos.md)
- [Capturing Uncompressed Image Data](capturing-uncompressed-image-data.md)
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)
- [Capturing Photos with Depth](capturing-photos-with-depth.md)

#### Discussion

Use this method to receive the results of photo capture regardless of format.

> ❗ **Important**:  Implementing this method is recommended for all still image (as opposed to Live Photo) capture workflows, and required if you request depth data delivery. The photo output validates this requirement when you call its [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method; if your delegate does not implement the correct methods, the photo output raises an exception.

 Implementing this method is recommended for all still image (as opposed to Live Photo) capture workflows, and required if you request depth data delivery. The photo output validates this requirement when you call its [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method; if your delegate does not implement the correct methods, the photo output raises an exception.

The photo output calls this method once for each primary image to be delivered in a capture request. If you request capture in both RAW and processed formats, this method fires once for each format. If you request a bracketed capture with multiple exposures, this method fires once for each exposure.

## Parameters

- `output`: The photo output performing the capture.
- `photo`: This parameter is always non- : if an error prevented successful capture, this object still contains metadata for the intended capture.
- `error`: If the capture process could not proceed successfully, an error object describing the failure; otherwise,  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:))*