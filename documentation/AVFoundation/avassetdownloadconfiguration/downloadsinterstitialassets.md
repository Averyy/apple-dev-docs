# downloadsInterstitialAssets

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL downloadsInterstitialAssets;
```

## Discussion

Ordinarily, interstitial assets are skipped when downloading content for later playback. Setting this property to true will cause interstitial assets to be downloaded as well. Playback of the downloaded content can then match the experience of online streaming playback as closely as possible.

## See Also

### Accessing configuration details
- [var artworkData: Data?](./artworkdata.md)
  A data value that represents the asset’s artwork.
- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](./primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration]](./auxiliarycontentconfigurations.md)
  The configuration for the auxiliary content that the task downloads.
- [class AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md)
  A configuration object that contains variant qualifiers and media options.
- [var optimizesAuxiliaryContentConfigurations: Bool](./optimizesauxiliarycontentconfigurations.md)
  A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](./setinterstitialmediaselectioncriteria%28_,formediacharacteristic%29.md)
  Sets media selection on interstitials for this asset


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/downloadsinterstitialassets)*