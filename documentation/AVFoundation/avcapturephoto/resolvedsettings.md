# resolvedSettings

**Framework**: AVFoundation  
**Kind**: property

The settings object that was used to request this photo capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var resolvedSettings: AVCaptureResolvedPhotoSettings { get }
```

#### Discussion

To determine which [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) call produced this photo capture result, match this [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object’s [`uniqueID`](avcaptureresolvedphotosettings/uniqueid.md) value to the [`uniqueID`](avcapturephotosettings/uniqueid.md) property of the photo settings object you requested capture with. You can also use this object to find out which values the photo output has chosen for automatic settings.

## See Also

- [var photoCount: Int](avcapturephoto/photocount.md)
  The 1-based index of this photo capture relative to other results from the same capture request.
- [var timestamp: CMTime](avcapturephoto/timestamp.md)
  The time at which the image was captured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/resolvedsettings)*