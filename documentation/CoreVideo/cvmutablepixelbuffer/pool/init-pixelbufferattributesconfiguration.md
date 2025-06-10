# init(pixelBufferAttributes:configuration:)

**Framework**: Core Video  
**Kind**: init

Create a new pixel buffer pool which creates pixel buffers using `pixelBufferAttributes`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(pixelBufferAttributes attributes: CVPixelBufferCreationAttributes, configuration: CVMutablePixelBuffer.Pool.Configuration = .init()) throws
```

## Parameters

- `configuration`: Change how the pool allocates and reuses pixel buffer backings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/init(pixelbufferattributes:configuration:))*