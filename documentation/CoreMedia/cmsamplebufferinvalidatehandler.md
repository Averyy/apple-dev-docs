# CMSampleBufferInvalidateHandler

**Framework**: Core Media  
**Kind**: typealias

Client callback called by [`CMSampleBufferInvalidate(_:)`](cmsamplebufferinvalidate(_:).md).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMSampleBufferInvalidateHandler = (CMSampleBuffer) -> Void
```

## Parameters

- `sbuf`: The   being invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatehandler)*