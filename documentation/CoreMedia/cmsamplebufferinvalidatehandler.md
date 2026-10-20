# CMSampleBufferInvalidateHandler

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

Client callback called by [`CMSampleBufferInvalidate(_:)`](./cmsamplebufferinvalidate%28_%29.md).

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

```c
typedef void (^)(struct opaqueCMSampleBuffer *) CMSampleBufferInvalidateHandler;
```

## Parameters

- `sbuf`: The `CMSampleBuffer` being invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidatehandler)*