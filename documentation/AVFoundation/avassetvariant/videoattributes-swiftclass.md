# AVAssetVariant.VideoAttributes

**Framework**: AVFoundation  
**Kind**: class

An object that defines the video attributes for an asset variant.

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
class VideoAttributes
```

## Topics

### Inspecting the Attributes
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
- [var videoLayoutAttributes: [AVAssetVariant.VideoAttributes.LayoutAttributes]](avassetvariant/videoattributes-swift.class/videolayoutattributes.md)
  Attributes that describe the layout of the video content.
- [AVAssetVariant.VideoAttributes.LayoutAttributes](avassetvariant/videoattributes-swift.class/layoutattributes.md)
  Attributes that describe the layout of video content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var audioAttributes: AVAssetVariant.AudioAttributes?](avassetvariant/audioattributes-swift.property.md)
  The audio rendition attributes for the variant.
- [AVAssetVariant.AudioAttributes](avassetvariant/audioattributes-swift.class.md)
  An object that defines the audio attributes for an asset variant.
- [var videoAttributes: AVAssetVariant.VideoAttributes?](avassetvariant/videoattributes-swift.property.md)
  The video rendition attributes for the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class)*