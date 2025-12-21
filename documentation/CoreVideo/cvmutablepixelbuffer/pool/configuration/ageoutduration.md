# ageOutDuration

**Framework**: Core Video  
**Kind**: property

Backing memory of released buffers is kept around for this duration before being freed (default is 1 second). If set to 0, the backing memory of released buffers is freed immediately.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var ageOutDuration: TimeInterval
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/configuration/ageoutduration)*