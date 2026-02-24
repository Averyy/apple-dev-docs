# photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)

**Framework**: AVFoundation  
**Kind**: method

Provides the delegate a captured image in RAW format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingRawPhoto rawSampleBuffer: CMSampleBuffer?, previewPhoto previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)
```

#### Discussion

Use this method to receive the results of a RAW format capture. (If you request capture in both RAW and a processed format, the photo output calls both this method and the [`photoOutput(_:didFinishProcessingPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) method.)

> ❗ **Important**:  You must implement either this method or the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method if you request capture in a RAW format. The photo output validates this requirement when you call its [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method; if your delegate does not implement the correct methods, the photo output raises an exception.

If you request RAW format capture, the photo output calls this method once for each exposure in the capture request. If you request a single image capture, this method is called once. If you request a bracketed capture with multiple exposures, this method is called once for each exposure.

## Parameters

- `output`: The photo output performing the capture.
- `rawSampleBuffer`: A sample buffer containing the captured RAW image. The format of this buffer matches the format you requested for the RAW image (see the [`rawPhotoPixelFormatType`](avcapturephotosettings/rawphotopixelformattype.md) property of your photo settings). If an error prevented successful capture, this parameter is `nil`—see the `error` parameter for a description of the failure.
- `previewPhotoSampleBuffer`: If you requested a thumbnail-sized version of the photo (with the [`previewPhotoFormat`](avcapturephotosettings/previewphotoformat.md) property of your photo settings object), a sample buffer containing the thumbnail photo in the requested format. If you did not request preview delivery, or if an error prevented capture, this parameter is `nil`.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s [`uniqueID`](avcapturephotosettings/uniqueid.md) value to the [`uniqueID`](avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.
- `bracketSettings`: If you requested a bracketed capture of multiple images with a [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md), a bracketed still image settings object describing which image in the bracket this delegate call corresponds to. If you did not request bracketed capture, this parameter is `nil`.
- `error`: If an the capture process could not proceed successfully, an error object describing the failure; otherwise, `nil`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:))*