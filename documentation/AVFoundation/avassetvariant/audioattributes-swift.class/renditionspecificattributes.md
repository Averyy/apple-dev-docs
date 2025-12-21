# AVAssetVariant.AudioAttributes.RenditionSpecificAttributes

**Framework**: AVFoundation  
**Kind**: class

An object that represents attributes specific to a particular rendition.

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
class RenditionSpecificAttributes
```

## Topics

### Accessing attributes
- [var channelCount: Int?](avassetvariant/audioattributes-swift.class/renditionspecificattributes/channelcount.md)
  The count of audio channels in the rendition.
- [var isBinaural: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isbinaural.md)
  A Boolean value that indicates the variant is best suited for delivery to headphones.
- [var isImmersive: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isimmersive.md)
  A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [var isDownmix: Bool](avassetvariant/audioattributes-swift.class/renditionspecificattributes/isdownmix.md)
  A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.

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

- [var formatIDs: [AudioFormatID]](avassetvariant/audioattributes-swift.class/formatids.md)
  The audio formats of the renditions present in the variant.
- [func renditionSpecificAttributes(for: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?](avassetvariant/audioattributes-swift.class/renditionspecificattributes(for:).md)
  Returns specific attributes for the media option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes)*