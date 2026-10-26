# PHImageResultIsDegradedKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates whether the result image is a low-quality substitute for the requested image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHImageResultIsDegradedKey: String
```

```c
extern NSString * const PHImageResultIsDegradedKey;
```

#### Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSNumber` object containing a Boolean value.If `true`, the `result` parameter of your `resultHandler` block contains a low-quality image because Photos could not yet provide a higher-quality image. Depending on your settings in the [`PHImageRequestOptions`](./phimagerequestoptions.md) object that you provided with the request, Photos may call your result handler block again to provide a higher-quality image.

## See Also

### Constants
- [let PHImageResultIsInCloudKey: String](./phimageresultisincloudkey.md)
  A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [let PHImageResultRequestIDKey: String](./phimageresultrequestidkey.md)
  A key whose value is a unique identifier for the image request.
- [let PHImageCancelledKey: String](./phimagecancelledkey.md)
  A key whose value indicates whether the image request was canceled.
- [let PHImageErrorKey: String](./phimageerrorkey.md)
  A key whose value is an error that occurred when Photos attempted to load the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimageresultisdegradedkey)*