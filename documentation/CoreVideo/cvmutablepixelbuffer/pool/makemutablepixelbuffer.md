# makeMutablePixelBuffer(_:)

**Framework**: Core Video  
**Kind**: method

This function creates a new CVMutablePixelBuffer using the pixel buffer attributes specified during pool creation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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