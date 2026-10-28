# AVAssetDownloadTaskMinimumRequiredPresentationSizeKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key that indicates the minimum presentation size of the variant to download.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetDownloadConfiguration:variantQualifiers with predicateForPresentationWidth and predicateForPresentationHeight instead

## Declaration

```swift
let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String
```

```c
extern NSString * const AVAssetDownloadTaskMinimumRequiredPresentationSizeKey;
```

## Discussion

By default, a download task selects the variant with the largest media presentation size. To download a variant of a particular size, provide a [`CGSize`](../CoreFoundation/cgsize.md) value for this key.

## See Also

### Download option keys
- [let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String](./avassetdownloadtaskminimumrequiredmediabitratekey.md)
  A key that indicates the minimum bit rate of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](./avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String](./avassetdownloadtaskmediaselectionprefersmultichannelkey.md)
  A key that indicates whether the task downloads media selections with support for multichannel playback, when available.
- [let AVAssetDownloadTaskPrefersHDRKey: String](./avassetdownloadtaskprefershdrkey.md)
  A key that indicates whether the task downloads HDR instead of SDR video, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](./avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredpresentationsizekey)*