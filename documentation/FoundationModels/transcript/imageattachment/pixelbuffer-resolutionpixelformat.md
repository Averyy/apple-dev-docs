# pixelBuffer(resolution:pixelFormat:)

**Framework**: Foundation Models  
**Kind**: method

Returns the image as a `CVPixelBuffer`, optionally resampled to a given resolution and pixel format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func pixelBuffer(resolution: CGSize? = nil, pixelFormat: OSType? = nil) throws -> CVReadOnlyPixelBuffer
```

## Parameters

- `resolution`: The desired resolution of the pixel buffer. Default behavior will use the image’s original resolution.
- `pixelFormat`: The pixel format of the pixel buffer. Defaults to `kCVPixelFormatType_32BGRA`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/imageattachment/pixelbuffer(resolution:pixelformat:))*