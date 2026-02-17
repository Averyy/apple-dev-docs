# downloadsInterstitialAssets

**Framework**: AVFoundation  
**Kind**: property

Download interstitial assets as listed in the index file. False by default.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var downloadsInterstitialAssets: Bool { get set }
```

#### Discussion

Ordinarily, interstitial assets are skipped when downloading content for later playback. Setting this property to true will cause interstitial assets to be downloaded as well. Playback of the downloaded content can then match the experience of online streaming playback as closely as possible.

## See Also

- [var artworkData: Data?](avassetdownloadconfiguration/artworkdata.md)
  A data value that represents the asset’s artwork.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/downloadsinterstitialassets)*