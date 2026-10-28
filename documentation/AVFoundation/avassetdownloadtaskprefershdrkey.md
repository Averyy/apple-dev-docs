# AVAssetDownloadTaskPrefersHDRKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether the task downloads HDR instead of SDR video, when available.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetDownloadConfiguration:variantQualifiers with assetVariantQualifierWithPredicate using [NSPredicate predicateWithFormat:@'videoAttributes.videoRange == %@', AVVideoRangePQ]

## Declaration

```swift
let AVAssetDownloadTaskPrefersHDRKey: String
```

```c
extern NSString * const AVAssetDownloadTaskPrefersHDRKey;
```

## Discussion

By default, a download task prefers downloading HDR content. Provide a Boolean value of [`false`](../Swift/false.md) to change this behavior.

## See Also

### Download option keys
- [let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String](./avassetdownloadtaskminimumrequiredmediabitratekey.md)
  A key that indicates the minimum bit rate of the variant to download.
- [let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String](./avassetdownloadtaskminimumrequiredpresentationsizekey.md)
  A key that indicates the minimum presentation size of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](./avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String](./avassetdownloadtaskmediaselectionprefersmultichannelkey.md)
  A key that indicates whether the task downloads media selections with support for multichannel playback, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](./avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskprefershdrkey)*