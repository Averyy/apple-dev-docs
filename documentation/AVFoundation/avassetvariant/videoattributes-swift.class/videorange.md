# videoRange

**Framework**: AVFoundation  
**Kind**: property

The video range of the variant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var videoRange: AVVideoRange { get }
```

#### Discussion

The property defaults to [`sdr`](avvideorange/sdr.md).

## See Also

- [var codecTypes: [CMVideoCodecType]](avassetvariant/videoattributes-swift.class/codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](avassetvariant/videoattributes-swift.class/nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](avassetvariant/videoattributes-swift.class/presentationsize.md)
  The presentation size of the variant’s renditions.
- [struct AVVideoRange](avvideorange.md)
  Constants that describe a video variant’s dynamic range.
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](avassetvariant/videoattributes-swift.class/videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](avassetvariant/videoattributes-swift.class/layoutattributes.md)
  Attributes that describe the layout of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videorange)*