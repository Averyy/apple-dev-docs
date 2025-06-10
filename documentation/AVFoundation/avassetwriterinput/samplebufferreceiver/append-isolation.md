# append(_:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the sample buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func append(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `sampleBuffer`: The sample buffer to be appended.
- `isolation`: The actor on which this async function should be isolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append(_:isolation:))*