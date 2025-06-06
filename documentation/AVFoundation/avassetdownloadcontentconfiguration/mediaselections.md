# mediaSelections

**Framework**: AVFoundation  
**Kind**: property

The media selections of an asset that a task downloads.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var mediaSelections: [AVMediaSelection] { get set }
```

#### Discussion

If your configuration doesn’t indicate a media selection, the system uses the asset’s automatic media selection.

## See Also

- [var variantQualifiers: [AVAssetVariantQualifier]](avassetdownloadcontentconfiguration/variantqualifiers.md)
  The variant qualifiers for this configuration.
- [class AVAssetVariantQualifier](avassetvariantqualifier.md)
  An object that represents an HTTP Live Streaming asset variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadcontentconfiguration/mediaselections)*