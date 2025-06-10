# expectedPhotoCount

**Framework**: AVFoundation  
**Kind**: property

The number of photo capture results in the capture request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var expectedPhotoCount: Int { get }
```

## Mentions

- [Tracking Photo Capture Progress](tracking-photo-capture-progress.md)
- [Capturing a Bracketed Photo Sequence](capturing-a-bracketed-photo-sequence.md)

#### Discussion

When you request a photo capture, the photo output calls your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method many times based on the settings you choose. For example, if you request a bracket of three exposures with image delivery in both JPEG and RAW formats, the expected photo count is `6`.

The [`photoCount`](avcapturephoto/photocount.md) property of each [`AVCapturePhoto`](avcapturephoto.md) object delivered to your delegate indicates where that capture result relates to this sequence. When your delegate receives a photo whose [`photoCount`](avcapturephoto/photocount.md) value matches the [`expectedPhotoCount`](avcaptureresolvedphotosettings/expectedphotocount.md), you know you’ve received the last one for the given capture request.

## See Also

- [var uniqueID: Int64](avcaptureresolvedphotosettings/uniqueid.md)
  The unique identifier for the photo capture this settings object corresponds to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/expectedphotocount)*