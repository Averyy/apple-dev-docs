# makeDataReady(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads sample data asynchronously for all sample buffers within a batch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func makeDataReady() async throws
```

#### Discussion

Calling this method more than once on a batch generates an exception.

## Parameters

- `completionHandler`: A callback the system invokes once when all sample buffers in the batch are data-ready, or when an error occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch/makedataready(completionhandler:))*