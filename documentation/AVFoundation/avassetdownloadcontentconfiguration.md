# AVAssetDownloadContentConfiguration

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A configuration object that contains variant qualifiers and media options.

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
class AVAssetDownloadContentConfiguration
```

```objc
@interface AVAssetDownloadContentConfiguration : NSObject
```

## Topics

### Accessing configuration details
- [var variantQualifiers: [AVAssetVariantQualifier]](./avassetdownloadcontentconfiguration/variantqualifiers.md)
  The variant qualifiers for this configuration.
- [class AVAssetVariantQualifier](./avassetvariantqualifier.md)
  An object that represents an HTTP Live Streaming asset variant.
- [var mediaSelections: [AVMediaSelection]](./avassetdownloadcontentconfiguration/mediaselections.md)
  The media selections of an asset that a task downloads.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing configuration details
- [var artworkData: Data?](./avassetdownloadconfiguration/artworkdata.md)
  A data value that represents the asset’s artwork.
- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](./avassetdownloadconfiguration/primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration]](./avassetdownloadconfiguration/auxiliarycontentconfigurations.md)
  The configuration for the auxiliary content that the task downloads.
- [var optimizesAuxiliaryContentConfigurations: Bool](./avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.md)
  A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [var downloadsInterstitialAssets: Bool](./avassetdownloadconfiguration/downloadsinterstitialassets.md)
  Download interstitial assets as listed in the index file. False by default.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](./avassetdownloadconfiguration/setinterstitialmediaselectioncriteria%28_,formediacharacteristic%29.md)
  Sets media selection on interstitials for this asset


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadcontentconfiguration)*