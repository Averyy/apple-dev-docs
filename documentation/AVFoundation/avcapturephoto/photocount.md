# photoCount

**Framework**: AVFoundation  
**Kind**: property

The 1-based index of this photo capture relative to other results from the same capture request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var photoCount: Int { get }
```

## Mentions

- [Capturing a bracketed photo sequence](capturing-a-bracketed-photo-sequence.md)
- [Tracking photo capture progress](tracking-photo-capture-progress.md)

#### Discussion

The [`expectedPhotoCount`](avcaptureresolvedphotosettings/expectedphotocount.md) property of this capture result’s [`resolvedSettings`](avcapturephoto/resolvedsettings.md) object indicates the total number of images that will be returned for a given capture request. When your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method receives a photo whose [`photoCount`](avcapturephoto/photocount.md) value  matches the [`expectedPhotoCount`](avcaptureresolvedphotosettings/expectedphotocount.md) value, you know you’ve received the last one for the given capture request.

## See Also

- [var resolvedSettings: AVCaptureResolvedPhotoSettings](avcapturephoto/resolvedsettings.md)
  The settings object that was used to request this photo capture.
- [var timestamp: CMTime](avcapturephoto/timestamp.md)
  The time at which the image was captured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/photocount)*