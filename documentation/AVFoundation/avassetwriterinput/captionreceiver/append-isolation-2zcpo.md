# append(_:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the caption.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func append(_ caption: AVCaption, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `caption`: The caption to be appended.
- `isolation`: The actor on which this async function should be isolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/append(_:isolation:)-2zcpo)*