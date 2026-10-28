# PHImageResultRequestIDKey

**Framework**: Photos  
**Kind**: var  
**Role**: Global Variable

A key whose value is a unique identifier for the image request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
let PHImageResultRequestIDKey: String
```

```c
extern NSString * const PHImageResultRequestIDKey;
```

## Discussion

This key provides information about an image loading result in the `resultHandler` block for methods listed in Requesting Images. The corresponding value is an `NSNumber` object containing an integer value.This identifier matches that returned when making a request. You can use it with the [`cancelImageRequest(_:)`](./phimagemanager/cancelimagerequest%28_%29.md) method to cancel requests with pending results that are no longer needed.

## See Also

### Constants
- [let PHImageResultIsInCloudKey: String](./phimageresultisincloudkey.md)
  A key whose value indicates whether photo asset data is stored on the local device or must be downloaded from iCloud.
- [let PHImageResultIsDegradedKey: String](./phimageresultisdegradedkey.md)
  A key whose value indicates whether the result image is a low-quality substitute for the requested image.
- [let PHImageCancelledKey: String](./phimagecancelledkey.md)
  A key whose value indicates whether the image request was canceled.
- [let PHImageErrorKey: String](./phimageerrorkey.md)
  A key whose value is an error that occurred when Photos attempted to load the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimageresultrequestidkey)*