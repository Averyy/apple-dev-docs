# Result Handler Info Dictionary Keys

**Framework**: PhotoKit  
**Role**: API Collection

Info describing an attempt to load a Live Photo.

#### Overview

These keys are in the `info` dictionary of the result handler you provide for the [`request(withResourceFileURLs:placeholderImage:targetSize:contentMode:resultHandler:)`](https://developer.apple.com/documentation/photos/phlivephoto/request(withresourcefileurls:placeholderimage:targetsize:contentmode:resulthandler:)) method.

## Topics

### Constants
- [let PHLivePhotoInfoErrorKey: String](https://developer.apple.com/documentation/photos/phlivephotoinfoerrorkey)
  An error that occurred while attempting to load the requested Live Photo.
- [let PHLivePhotoInfoIsDegradedKey: String](https://developer.apple.com/documentation/photos/phlivephotoinfoisdegradedkey)
  A Boolean (`NSNumber`) value indicating whether the result Live Photo is a low-quality substitute for the requested Live Photo.
- [let PHLivePhotoInfoCancelledKey: String](https://developer.apple.com/documentation/photos/phlivephotoinfocancelledkey)
  A Boolean (`NSNumber`) value indicating whether the Live Photo loading request was canceled.

## See Also

### Constants
- [typealias PHLivePhotoRequestID](https://developer.apple.com/documentation/photos/phlivephotorequestid)
  A numeric identifier for an asynchronous Live Photo loading request.
- [Image Request Identifiers](./image-request-identifiers.md)
  Special values for the Live Photo request ID that are returned by asynchronous requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/result-handler-info-dictionary-keys)*