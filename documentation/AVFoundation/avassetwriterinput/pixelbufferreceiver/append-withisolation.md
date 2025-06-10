# append(_:with:isolation:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the pixel buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func append(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime, isolation: isolated (any Actor)? = #isolation) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `pixelBuffer`: The pixel buffer to be appended.
- `presentationTime`: The presentation time for the pixel buffer to be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/append(_:with:isolation:))*