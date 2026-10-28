# AVAssetDownloadTaskMinimumRequiredMediaBitrateKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key that indicates the minimum bit rate of the variant to download.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetDownloadConfiguration:variantQualifiers with assetVariantQualifierWithPredicate using desired comparison value against averageBitRate/peakBitRate instead

## Declaration

```swift
let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String
```

```c
extern NSString * const AVAssetDownloadTaskMinimumRequiredMediaBitrateKey;
```

## Discussion

By default, a download task selects the highest bit rate variant available. To download a variant of a particular size, provide an [`NSNumber`](../Foundation/nsnumber.md) value that indicates the preferred bit rate.

## See Also

### Download option keys
- [let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String](./avassetdownloadtaskminimumrequiredpresentationsizekey.md)
  A key that indicates the minimum presentation size of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](./avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String](./avassetdownloadtaskmediaselectionprefersmultichannelkey.md)
  A key that indicates whether the task downloads media selections with support for multichannel playback, when available.
- [let AVAssetDownloadTaskPrefersHDRKey: String](./avassetdownloadtaskprefershdrkey.md)
  A key that indicates whether the task downloads HDR instead of SDR video, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](./avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey)*