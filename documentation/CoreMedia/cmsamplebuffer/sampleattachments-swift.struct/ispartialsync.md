# isPartialSync

**Framework**: Core Media  
**Kind**: property

Indicates whether the sample is a partial sync sample.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var isPartialSync: Bool { get set }
```

#### Discussion

A partial sync sample can be decoded without requiring any previous samples to have been decoded. Samples following two consecutive partial sync samples also do not require samples prior to the pair to have been decoded. To treat a sample as a partial sync sample, set to true for both this key and the `notSync` key.

This attachment is read from and written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/ispartialsync)*