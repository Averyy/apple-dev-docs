# optimizesAuxiliaryContentConfigurations

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the task optimizes auxiliary content selection.

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
var optimizesAuxiliaryContentConfigurations: Bool { get set }
```

#### Discussion

By default, a download task optimizes its selection of auxiliary content based on its primary download content. For example, if the primary content configuration represents stereo renditions, and auxiliary content configuration represents multichannel audio renditions, the task choses the auxiliary multichannel variant to avoid downloading duplicate video renditions.

## See Also

- [var artworkData: Data?](avassetdownloadconfiguration/artworkdata.md)
  A data value that represents the asset’s artwork.
- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](avassetdownloadconfiguration/primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration]](avassetdownloadconfiguration/auxiliarycontentconfigurations.md)
  The configuration for the auxiliary content that the task downloads.
- [class AVAssetDownloadContentConfiguration](avassetdownloadcontentconfiguration.md)
  A configuration object that contains variant qualifiers and media options.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(_:formediacharacteristic:).md)
  Sets media selection on interstitials for this asset


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations)*