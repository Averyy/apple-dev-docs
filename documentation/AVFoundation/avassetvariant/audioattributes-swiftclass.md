# AVAssetVariant.AudioAttributes

**Framework**: AVFoundation  
**Kind**: class

An object that defines the audio attributes for an asset variant.

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
class AudioAttributes
```

## Topics

### Inspecting audio attributes
- [var formatIDs: [AudioFormatID]](avassetvariant/audioattributes-swift.class/formatids.md)
  The audio formats of the renditions present in the variant.
- [func renditionSpecificAttributes(for: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?](avassetvariant/audioattributes-swift.class/renditionspecificattributes(for:).md)
  Returns specific attributes for the media option.
- [AVAssetVariant.AudioAttributes.RenditionSpecificAttributes](avassetvariant/audioattributes-swift.class/renditionspecificattributes.md)
  An object that represents attributes specific to a particular rendition.

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
- [var videoAttributes: AVAssetVariant.VideoAttributes?](avassetvariant/videoattributes-swift.property.md)
  The video rendition attributes for the variant.
- [AVAssetVariant.VideoAttributes](avassetvariant/videoattributes-swift.class.md)
  An object that defines the video attributes for an asset variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class)*