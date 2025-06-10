# append(_:with:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the tagged pixel buffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func append(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `taggedPixelBufferGroup`: The tagged pixel buffers to be appended.
- `presentationTime`: The presentation time for the tagged pixel buffers to be appended.
- `isolation`: The actor on which this async function should be isolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:isolation:))*