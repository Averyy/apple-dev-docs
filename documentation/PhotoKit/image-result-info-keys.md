# Image Result Info Keys

**Framework**: PhotoKit  
**Role**: API Collection

Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.

## Topics

### Constants
- [let PHImageResultIsInCloudKey: String](https://developer.apple.com/documentation/photos/phimageresultisincloudkey)
  A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [let PHImageResultIsDegradedKey: String](https://developer.apple.com/documentation/photos/phimageresultisdegradedkey)
  A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [let PHImageResultRequestIDKey: String](https://developer.apple.com/documentation/photos/phimageresultrequestidkey)
  A key whose value is a unique identifier for the image request.
- [let PHImageCancelledKey: String](https://developer.apple.com/documentation/photos/phimagecancelledkey)
  A key whose value indicates whether the image request was canceled.
- [let PHImageErrorKey: String](https://developer.apple.com/documentation/photos/phimageerrorkey)
  A key whose value is an error that occurred when Photos attempted to load the image.

## See Also

### Constants
- [enum PHImageContentMode](https://developer.apple.com/documentation/photos/phimagecontentmode)
  Options for fitting an image’s aspect ratio to a requested size, used by the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](https://developer.apple.com/documentation/photos/phimagemanager/requestimage(for:targetsize:contentmode:options:resulthandler:)) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/image-result-info-keys)*