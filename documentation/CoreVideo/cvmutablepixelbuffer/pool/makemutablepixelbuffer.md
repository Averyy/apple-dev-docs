# makeMutablePixelBuffer(_:)

**Framework**: Core Video  
**Kind**: method

This function creates a new CVMutablePixelBuffer using the pixel buffer attributes specified during pool creation.

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
final func makeMutablePixelBuffer(_ attributes: CVMutablePixelBuffer.Pool.AllocationAttributes = .init()) throws -> CVMutablePixelBuffer
```

#### Discussion

- Returns A new mutable pixel buffer created with creationAttributes passed to [`init(pixelBufferAttributes:configuration:)`](cvmutablepixelbuffer/pool/init(pixelbufferattributes:configuration:).md)

## Parameters

- `attributes`: Attributes which control how pixel buffers are allocated


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool/makemutablepixelbuffer(_:))*