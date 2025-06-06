# renditionSpecificAttributes(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns specific attributes for the media option.

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
func renditionSpecificAttributes(for mediaSelectionOption: AVMediaSelectionOption) -> AVAssetVariant.AudioAttributes.RenditionSpecificAttributes?
```

#### Return Value

Attributes for the rendition, or `nil` of none exist.

## Parameters

- `mediaSelectionOption`: The media option for which to retrieve attributes.

## See Also

- [var formatIDs: [AudioFormatID]](avassetvariant/audioattributes-swift.class/formatids.md)
  The audio formats of the renditions present in the variant.
- [AVAssetVariant.AudioAttributes.RenditionSpecificAttributes](avassetvariant/audioattributes-swift.class/renditionspecificattributes.md)
  An object that represents attributes specific to a particular rendition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariant/audioattributes-swift.class/renditionspecificattributes(for:))*