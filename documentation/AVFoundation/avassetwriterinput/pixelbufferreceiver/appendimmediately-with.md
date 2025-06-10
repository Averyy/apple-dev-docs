# appendImmediately(_:with:)

**Framework**: AVFoundation  
**Kind**: method

Appends the pixel buffer synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func appendImmediately(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `pixelBuffer`: The pixel buffer to be appended.
- `presentationTime`: The presentation time for the pixel buffer to be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:))*