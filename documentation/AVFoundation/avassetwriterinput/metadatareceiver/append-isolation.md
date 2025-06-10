# append(_:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the timed metadata group.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func append(_ timedMetadataGroup: AVTimedMetadataGroup, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `timedMetadataGroup`: The timed metadata group to be appended.
- `isolation`: The actor on which this async function should be isolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/append(_:isolation:))*