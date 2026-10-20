# auxiliaryContentConfigurations

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The configuration for the auxiliary content that the task downloads.

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
var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVAssetDownloadContentConfiguration *> * auxiliaryContentConfigurations;
```

## See Also

### Accessing configuration details
- [var artworkData: Data?](./artworkdata.md)
  A data value that represents the asset’s artwork.
- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](./primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [class AVAssetDownloadContentConfiguration](../avassetdownloadcontentconfiguration.md)
  A configuration object that contains variant qualifiers and media options.
- [var optimizesAuxiliaryContentConfigurations: Bool](./optimizesauxiliarycontentconfigurations.md)
  A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [var downloadsInterstitialAssets: Bool](./downloadsinterstitialassets.md)
  Download interstitial assets as listed in the index file. False by default.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](./setinterstitialmediaselectioncriteria%28_,formediacharacteristic%29.md)
  Sets media selection on interstitials for this asset


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/auxiliarycontentconfigurations)*