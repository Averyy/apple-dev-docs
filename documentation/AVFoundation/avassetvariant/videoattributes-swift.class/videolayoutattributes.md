# videoLayoutAttributes

**Framework**: AVFoundation  
**Kind**: property

Attributes that describe the layout of the video content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes] { get }
```

#### Discussion

This property may contain more that one element if the variant contains a collection of differing video layout media attributes over time.

## See Also

- [var codecTypes: [CMVideoCodecType]](avassetvariant/videoattributes-swift.class/codectypes.md)
  The video sample codec types present in the variant’s renditions.
- [var nominalFrameRate: Double?](avassetvariant/videoattributes-swift.class/nominalframerate.md)
  The nominal frame rate of the variant’s renditions.
- [var presentationSize: CGSize](avassetvariant/videoattributes-swift.class/presentationsize.md)
  The presentation size of the variant’s renditions.
- [var videoRange: AVVideoRange](avassetvariant/videoattributes-swift.class/videorange.md)
  The video range of the variant.
- [struct AVVideoRange](avvideorange.md)
  Constants that describe a video variant’s dynamic range.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](avassetvariant/videoattributes-swift.class/layoutattributes.md)
  Attributes that describe the layout of video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/videolayoutattributes)*