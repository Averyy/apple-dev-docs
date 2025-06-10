# ageOutDuration

**Framework**: Core Video  
**Kind**: property

Backing memory of released buffers is kept around for this duration before being freed (default is 1 second). If set to 0, the backing memory of released buffers is freed immediately.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var ageOutDuration: TimeInterval
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/configuration/ageoutduration)*