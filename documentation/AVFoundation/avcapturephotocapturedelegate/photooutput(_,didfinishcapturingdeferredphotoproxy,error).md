# photoOutput(_:didFinishCapturingDeferredPhotoProxy:error:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the system finishes capturing the photo proxy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishCapturingDeferredPhotoProxy deferredPhotoProxy: AVCaptureDeferredPhotoProxy?, error: (any Error)?)
```

```objc
- (void) captureOutput:(AVCapturePhotoOutput *) output didFinishCapturingDeferredPhotoProxy:(AVCaptureDeferredPhotoProxy *) deferredPhotoProxy error:(NSError *) error;
```

#### Discussion

You can use the output’s [`fileDataRepresentation()`](../avcapturephoto/filedatarepresentation%28%29.md) with [`PHAssetCreationRequest`](../../Photos/phassetcreationrequest.md) to eventually produce the final, processed photo into the user’s Photo Library. Add the in-memory proxy file data representation to the photo library as quickly as possible after this call to ensure that the photo library can begin background processing. It’s also important so that the intermediates aren’t removed by a periodic clean-up job looking for abandoned intermediates produced by using the deferred photo processing APIs.

Your delegate implementation must adopt this method to opt into deferred photo processing, otherwise calling [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) throws an exception.

## Parameters

- `output`: The output instance.
- `deferredPhotoProxy`: A [`AVCaptureDeferredPhotoProxy`](../avcapturedeferredphotoproxy.md) instance that contains a proxy [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) as a placeholder for the final image.
- `error`: If the system couldn’t create the photo proxy, or any of the underlying intermediate files, an error object that describes the failure.

## See Also

### Receiving capture results
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: AVCapturePhoto, error: (any Error)?)](./photooutput%28_,didfinishprocessingphoto,error%29.md)
  Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishRecordingLivePhotoMovieForEventualFileAt: URL, resolvedSettings: AVCaptureResolvedPhotoSettings)](./photooutput%28_,didfinishrecordinglivephotomovieforeventualfileat,resolvedsettings%29.md)
  Notifies the delegate that the movie content of a Live Photo has finished recording.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingLivePhotoToMovieFileAt: URL, duration: CMTime, photoDisplayTime: CMTime, resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)](./photooutput%28_,didfinishprocessinglivephototomoviefileat,duration,photodisplaytime,resolvedsettings,error%29.md)
  Provides the delegate the movie file URL resulting from a Live Photo capture.
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](./photooutput%28_,didfinishprocessingphoto,previewphoto,resolvedsettings,bracketsettings,error%29.md)
  Provides the delegate a captured image in a processed format (such as JPEG).
- [func photoOutput(AVCapturePhotoOutput, didFinishProcessingRawPhoto: CMSampleBuffer?, previewPhoto: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)](./photooutput%28_,didfinishprocessingrawphoto,previewphoto,resolvedsettings,bracketsettings,error%29.md)
  Provides the delegate a captured image in RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:))*