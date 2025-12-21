# AVVideoRange

**Framework**: AVFoundation  
**Kind**: struct

Constants that describe a video variant’s dynamic range.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVVideoRange
```

## Topics

### Video ranges
- [static let pq: AVVideoRange](avvideorange/pq.md)
  Indicates Perceptual Quantizer (PQ) high-dynamic-range video.
- [static let hlg: AVVideoRange](avvideorange/hlg.md)
  Indicates Hybrid-Log Gamma (HLG) high-dynamic-range video.
- [static let sdr: AVVideoRange](avvideorange/sdr.md)
  Indicates standard-dynamic-range (SDR) video.
### Initializers
- [init(rawValue: String)](avvideorange/init(rawvalue:).md)
  Creates a video range with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var codecTypes: [CMVideoCodecType]](avassetvariant/videoattributes-swift.class/codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](avassetvariant/videoattributes-swift.class/nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](avassetvariant/videoattributes-swift.class/presentationsize.md)
  The presentation size of the variant’s renditions.
- [var videoRange: AVVideoRange](avassetvariant/videoattributes-swift.class/videorange.md)
  The video range of the variant.
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](avassetvariant/videoattributes-swift.class/videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](avassetvariant/videoattributes-swift.class/layoutattributes.md)
  Attributes that describe the layout of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideorange)*