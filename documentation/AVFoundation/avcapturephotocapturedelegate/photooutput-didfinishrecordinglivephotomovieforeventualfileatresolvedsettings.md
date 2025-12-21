# photoOutput(_:didFinishRecordingLivePhotoMovieForEventualFileAt:resolvedSettings:)

**Framework**: AVFoundation  
**Kind**: method

Notifies the delegate that the movie content of a Live Photo has finished recording.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishRecordingLivePhotoMovieForEventualFileAt outputFileURL: URL, resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Mentions

- [Capturing and saving Live Photos](capturing-and-saving-live-photos.md)

#### Discussion

The photo output calls this method as soon as it has captured all movie data for a Live Photo. However, at this moment, that media content has not yet been processed or written to storage. (To be notified when the complete movie file has finished writing and is ready for consumption, implement the [`photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md) method.)

Use this method to determine when it is appropriate to change your displayed UI to indicate that Live Photo movie capture is no longer in progress. For example, the Camera app displays a “LIVE” icon when the user presses the shutter button, then hides that icon when movie capture ends.

The photo output calls this method only once for each Live Photo capture.

## Parameters

- `output`: The photo output performing the capture.
- `outputFileURL`: The file URL at which the Live Photo movie will be written.
- `resolvedSettings`: An object describing the settings used for this capture. Match this object’s   value to the   property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: AVCapturePhoto, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md)
  Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingLivePhotoToMovieFileAt: URL, duration: CMTime, photoDisplayTime: CMTime, resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:).md)
  Provides the delegate the movie file URL resulting from a Live Photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishCapturingDeferredPhotoProxy: AVCaptureDeferredPhotoProxy?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:).md)
  Tells the delegate when the system finishes capturing the photo proxy.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:).md)
  Provides the delegate a captured image in a processed format (such as JPEG).
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingRawPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md)
  Provides the delegate a captured image in RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishrecordinglivephotomovieforeventualfileat:resolvedsettings:))*