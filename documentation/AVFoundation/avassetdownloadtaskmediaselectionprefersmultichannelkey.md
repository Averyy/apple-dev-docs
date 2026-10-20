# AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether the task downloads media selections with support for multichannel playback, when available.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetDownloadConfiguration:variantQualifiers with predicateForChannelCount instead

## Declaration

```swift
let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String
```

```c
extern NSString * const AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey;
```

#### Discussion

By default, download tasks retrieve the variant’s stereo audio and the most capable multichannel rendition available. Provide a Boolean value of [`false`](../Swift/false.md) to disable this behavior.

## See Also

### Download option keys
- [let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String](./avassetdownloadtaskminimumrequiredmediabitratekey.md)
  A key that indicates the minimum bit rate of the variant to download.
- [let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String](./avassetdownloadtaskminimumrequiredpresentationsizekey.md)
  A key that indicates the minimum presentation size of the variant to download.
- [let AVAssetDownloadTaskMediaSelectionKey: String](./avassetdownloadtaskmediaselectionkey.md)
  A key that indicates which media selection to download.
- [let AVAssetDownloadTaskPrefersHDRKey: String](./avassetdownloadtaskprefershdrkey.md)
  A key that indicates whether the task downloads HDR instead of SDR video, when available.
- [let AVAssetDownloadTaskPrefersLosslessAudioKey: String](./avassetdownloadtaskpreferslosslessaudiokey.md)
  A key that indicates whether the task downloads media selections in lossless audio format, when available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskmediaselectionprefersmultichannelkey)*