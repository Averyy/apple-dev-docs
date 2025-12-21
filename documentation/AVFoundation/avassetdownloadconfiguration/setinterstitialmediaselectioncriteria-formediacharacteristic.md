# setInterstitialMediaSelectionCriteria(_:forMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Sets media selection on interstitials for this asset

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func setInterstitialMediaSelectionCriteria(_ criteria: [AVPlayerMediaSelectionCriteria], forMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic)
```

#### Discussion

Typically, interstitial assets have not been discovered when the main download is initiated. This method allows the user to specify AVMediaSelectionCriteria for all interstitials that are discovered. Each AVPlayerMediaSelectionCriteria in the array of criteria specfies a set of criteria for a variant to download.

## Parameters

- `criteria`: The array of selection criteria to set
- `mediaCharacteristic`: The AVMediaCharacteristic to which the criteria will be applied

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadconfiguration/setinterstitialmediaselectioncriteria(_:formediacharacteristic:))*