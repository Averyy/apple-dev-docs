# AVAssetVariant.AudioAttributes

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetVariantAudioAttributes : NSObject
```

## Topics

### Inspecting audio attributes
- [var formatIDs: [AudioFormatID]](./audioattributes-swift.class/formatids.md)
  The audio formats of the renditions present in the variant.
- [func renditionSpecificAttributes(for: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?](./audioattributes-swift.class/renditionspecificattributes%28for%29.md)
  Returns specific attributes for the media option.
- [AVAssetVariant.AudioAttributes.RenditionSpecificAttributes](./audioattributes-swift.class/renditionspecificattributes.md)
  An object that represents attributes specific to a particular rendition.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring attributes
- [var audioAttributes: AVAssetVariant.AudioAttributes?](./audioattributes-swift.property.md)
  The audio rendition attributes for the variant.
- [var videoAttributes: AVAssetVariant.VideoAttributes?](./videoattributes-swift.property.md)
  The video rendition attributes for the variant.
- [AVAssetVariant.VideoAttributes](./videoattributes-swift.class.md)
  An object that defines the video attributes for an asset variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class)*