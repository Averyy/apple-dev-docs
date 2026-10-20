# AVAssetVariant.AudioAttributes.RenditionSpecificAttributes

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetVariantAudioRenditionSpecificAttributes : NSObject
```

## Topics

### Accessing attributes
- [var channelCount: Int?](./renditionspecificattributes/channelcount.md)
  The count of audio channels in the rendition.
- [var isBinaural: Bool](./renditionspecificattributes/isbinaural.md)
  A Boolean value that indicates the variant is best suited for delivery to headphones.
- [var isImmersive: Bool](./renditionspecificattributes/isimmersive.md)
  A Boolean value that indicates whether this variant contains virtualized or otherwise preprocessed audio content suitable for various purposes.
- [var isDownmix: Bool](./renditionspecificattributes/isdownmix.md)
  A Boolean value that indicates whether the variant is a downmix derivative of other media of greater channel count.

## Relationships

### Inherits From
- [NSObject](../../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting audio attributes
- [var formatIDs: [AudioFormatID]](./formatids.md)
  The audio formats of the renditions present in the variant.
- [func renditionSpecificAttributes(for: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?](./renditionspecificattributes%28for%29.md)
  Returns specific attributes for the media option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes)*