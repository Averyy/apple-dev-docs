# Image Result Info Keys

**Framework**: PhotoKit  
**Role**: API Collection

Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.

## Topics

### Constants
- [let PHImageResultIsInCloudKey: String](../Photos/phimageresultisincloudkey.md)
  A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [let PHImageResultIsDegradedKey: String](../Photos/phimageresultisdegradedkey.md)
  A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [let PHImageResultRequestIDKey: String](../Photos/phimageresultrequestidkey.md)
  A key whose value is a unique identifier for the image request.
- [let PHImageCancelledKey: String](../Photos/phimagecancelledkey.md)
  A key whose value indicates whether the image request was canceled.
- [let PHImageErrorKey: String](../Photos/phimageerrorkey.md)
  A key whose value is an error that occurred when Photos attempted to load the image.

## See Also

### Constants
- [enum PHImageContentMode](../Photos/phimagecontentmode.md)
  Options for fitting an image’s aspect ratio to a requested size, used by the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](../Photos/phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/image-result-info-keys)*