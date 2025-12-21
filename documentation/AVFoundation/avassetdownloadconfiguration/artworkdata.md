# artworkData

**Framework**: AVFoundation  
**Kind**: property

A data value that represents the asset’s artwork.

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
var artworkData: Data? { get set }
```

#### Discussion

The system displays this image in the usage pane of the Settings app.

## See Also

- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](avassetdownloadconfiguration/primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration]](avassetdownloadconfiguration/auxiliarycontentconfigurations.md)
  The configuration for the auxiliary content that the task downloads.
- [class AVAssetDownloadContentConfiguration](avassetdownloadcontentconfiguration.md)
  A configuration object that contains variant qualifiers and media options.
- [var optimizesAuxiliaryContentConfigurations: Bool](avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.md)
  A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(_:formediacharacteristic:).md)
  Sets media selection on interstitials for this asset


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/artworkdata)*