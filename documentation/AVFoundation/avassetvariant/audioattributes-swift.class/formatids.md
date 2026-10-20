# formatIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The audio formats of the renditions present in the variant.

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
@nonobjc
var formatIDs: [AudioFormatID] { get }
```

## See Also

### Inspecting audio attributes
- [func renditionSpecificAttributes(for: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?](./renditionspecificattributes%28for%29.md)
  Returns specific attributes for the media option.
- [AVAssetVariant.AudioAttributes.RenditionSpecificAttributes](./renditionspecificattributes.md)
  An object that represents attributes specific to a particular rendition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/formatids)*