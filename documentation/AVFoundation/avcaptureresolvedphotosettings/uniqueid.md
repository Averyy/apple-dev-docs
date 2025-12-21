# uniqueID

**Framework**: AVFoundation  
**Kind**: property

The unique identifier for the photo capture this settings object corresponds to.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var uniqueID: Int64 { get }
```

## Mentions

- [Tracking photo capture progress](tracking-photo-capture-progress.md)

#### Discussion

The value of this property matches the matches the [`uniqueID`](avcapturephotosettings/uniqueid.md) value of the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you passed when initiating a photo capture with the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. Use this value to determine which delegate method calls correspond to which capture requests.

## See Also

- [var expectedPhotoCount: Int](avcaptureresolvedphotosettings/expectedphotocount.md)
  The number of photo capture results in the capture request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/uniqueid)*