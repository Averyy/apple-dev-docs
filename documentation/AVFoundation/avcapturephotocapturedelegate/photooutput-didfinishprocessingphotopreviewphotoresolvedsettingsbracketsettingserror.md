# photoOutput(_:didFinishProcessingPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)

**Framework**: AVFoundation  
**Kind**: method

Provides the delegate a captured image in a processed format (such as JPEG).

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photoSampleBuffer: CMSampleBuffer?, previewPhoto previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)
```

#### Discussion

Use this method to receive the results of photo capture in a processed format such as JPEG. (If you request capture in both RAW and a processed format, the photo output calls both this method and the [`photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) method.)

> ❗ **Important**:  You must implement either this method or the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method if you request capture in a processed format. The photo output validates this requirement when you call its [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method; if your delegate does not implement the correct methods, the photo output raises an exception.

If you request capture in a processed format, the photo output calls this method once for each exposure in the capture request. If you request a single image capture, this method is called once. If you request a bracketed capture with multiple exposures, this method is called once for each exposure.

## Parameters

- `output`: The photo output performing the capture.
- `photoSampleBuffer`: If an error prevented successful capture, this parameter is  —see the   parameter for a description of the failure.
- `previewPhotoSampleBuffer`: If you requested a thumbnail-sized version of the photo (with the   property of your photo settings object), a sample buffer containing the thumbnail photo in the requested format. If you did not request preview delivery, or if an error prevented capture, this parameter is  .
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s   value to the   property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.
- `bracketSettings`: If you requested a bracketed capture of multiple images with a  , a bracketed still image settings object describing which image in the bracket this delegate call corresponds to. If you did not request bracketed capture, this parameter is  .
- `error`: If an the capture process could not proceed successfully, an error object describing the failure; otherwise,  .

## See Also

- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: AVCapturePhoto, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md)
  Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishRecordingLivePhotoMovieForEventualFileAt: URL, resolvedSettings: AVCaptureResolvedPhotoSettings)](avcapturephotocapturedelegate/photooutput(_:didfinishrecordinglivephotomovieforeventualfileat:resolvedsettings:).md)
  Notifies the delegate that the movie content of a Live Photo has finished recording.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingLivePhotoToMovieFileAt: URL, duration: CMTime, photoDisplayTime: CMTime, resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md)
  Provides the delegate the movie file URL resulting from a Live Photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishCapturingDeferredPhotoProxy: AVCaptureDeferredPhotoProxy?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:).md)
  Tells the delegate when the system finishes capturing the photo proxy.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingRawPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md)
  Provides the delegate a captured image in RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:))*