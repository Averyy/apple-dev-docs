# isNotSync

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample is a sync sample.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var isNotSync: Bool { get set }
```

#### Discussion

Set the value to true for samples which should not be treated as sync samples.

A sync sample, also known as a key frame or IDR (Instantaneous Decoding Refresh), can be decoded without requiring any previous samples to have been decoded. Samples following a sync sample also do not require samples prior to the sync sample to have been decoded. Samples are assumed to be sync samples by default.

This attachment is read from and written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/isnotsync)*