# PHImageErrorKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A key whose value is an error that occurred when Photos attempted to load the image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHImageErrorKey: String
```

```c
extern NSString * const PHImageErrorKey;
```

## Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSError` object.Photos provides an error object for this key if it cannot provide an image for your handler block’s `result` parameter. Examine the error object for information about the cause of the error.

## See Also

### Constants
- [let PHImageResultIsInCloudKey: String](./phimageresultisincloudkey.md)
  A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [let PHImageResultIsDegradedKey: String](./phimageresultisdegradedkey.md)
  A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [let PHImageResultRequestIDKey: String](./phimageresultrequestidkey.md)
  A key whose value is a unique identifier for the image request.
- [let PHImageCancelledKey: String](./phimagecancelledkey.md)
  A key whose value indicates whether the image request was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimageerrorkey)*