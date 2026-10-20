# AVAssetDownloadConfiguration

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that provides the configuration for a download task.

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
class AVAssetDownloadConfiguration
```

```objc
@interface AVAssetDownloadConfiguration : NSObject
```

## Topics

### Creating a configuration
- [convenience init(asset: AVURLAsset, title: String)](./avassetdownloadconfiguration/init%28asset,title%29.md)
  Creates a download configuration for a media asset.
### Accessing configuration details
- [var artworkData: Data?](./avassetdownloadconfiguration/artworkdata.md)
  A data value that represents the asset’s artwork.
- [var primaryContentConfiguration: AVAssetDownloadContentConfiguration](./avassetdownloadconfiguration/primarycontentconfiguration.md)
  The configuration for the primary content that the task downloads.
- [var auxiliaryContentConfigurations: [AVAssetDownloadContentConfiguration]](./avassetdownloadconfiguration/auxiliarycontentconfigurations.md)
  The configuration for the auxiliary content that the task downloads.
- [class AVAssetDownloadContentConfiguration](./avassetdownloadcontentconfiguration.md)
  A configuration object that contains variant qualifiers and media options.
- [var optimizesAuxiliaryContentConfigurations: Bool](./avassetdownloadconfiguration/optimizesauxiliarycontentconfigurations.md)
  A Boolean value that indicates whether the task optimizes auxiliary content selection.
- [var downloadsInterstitialAssets: Bool](./avassetdownloadconfiguration/downloadsinterstitialassets.md)
  Download interstitial assets as listed in the index file. False by default.
- [func setInterstitialMediaSelectionCriteria([AVPlayerMediaSelectionCriteria], forMediaCharacteristic: AVMediaCharacteristic)](./avassetdownloadconfiguration/setinterstitialmediaselectioncriteria%28_,formediacharacteristic%29.md)
  Sets media selection on interstitials for this asset

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating download tasks
- [func makeAssetDownloadTask(downloadConfiguration: AVAssetDownloadConfiguration) -> AVAssetDownloadTask](./avassetdownloadurlsession/makeassetdownloadtask%28downloadconfiguration%29.md)
  Creates a download task that uses the specified configuration.
- [func makeAssetDownloadTask(asset: AVURLAsset, assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAssetDownloadTask?](./avassetdownloadurlsession/makeassetdownloadtask%28asset,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset.
- [func aggregateAssetDownloadTask(with: AVURLAsset, mediaSelections: [AVMediaSelection], assetTitle: String, assetArtworkData: Data?, options: [String : Any]?) -> AVAggregateAssetDownloadTask?](./avassetdownloadurlsession/aggregateassetdownloadtask%28with,mediaselections,assettitle,assetartworkdata,options%29.md)
  Creates a download task to download the asset and media selections.
- [func makeAssetDownloadTask(asset: AVURLAsset, destinationURL: URL, options: [String : Any]?) -> AVAssetDownloadTask?](./avassetdownloadurlsession/makeassetdownloadtask%28asset,destinationurl,options%29.md)
  Creates a download task to download the asset to the indicated location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration)*