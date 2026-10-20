# CVMutablePixelBuffer.Pool

**Framework**: Core Video  
**Kind**: class  
**Role**: Class

Manage and recycle pixel buffer backings.

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
final class Pool
```

## Topics

### Structures
- [CVMutablePixelBuffer.Pool.AllocationAttributes](./pool/allocationattributes.md)
  Controls how new pixel buffers are allocated when `CVMutablePixelBuffer/Pool/mutablePixelBuffer(with:)` is called.
- [CVMutablePixelBuffer.Pool.Configuration](./pool/configuration.md)
  Configuration passed to pixel buffer pool on creation.
### Initializers
- [init(pixelBufferAttributes: CVPixelBufferCreationAttributes, configuration: CVMutablePixelBuffer.Pool.Configuration) throws](./pool/init%28pixelbufferattributes,configuration%29.md)
  Create a new pixel buffer pool which creates pixel buffers using `pixelBufferAttributes`.
- [init(unsafePool: sending CVPixelBufferPool)](./pool/init%28unsafepool%29.md)
  Initialize a mutable pixel buffer pool by transferring existing CVPixelBufferPool.
### Instance Properties
- [var pixelBufferAttributes: CVPixelBufferCreationAttributes](./pool/pixelbufferattributes.md)
  Creation attributes for the pixel buffers created by this pool.
### Instance Methods
- [func flush(agedOutOnly: Bool)](./pool/flush%28agedoutonly%29.md)
  Frees as many buffers from the pool as possible.
- [func makeMutablePixelBuffer(CVMutablePixelBuffer.Pool.AllocationAttributes) throws -> CVMutablePixelBuffer](./pool/makemutablepixelbuffer%28_%29.md)
  This function creates a new CVMutablePixelBuffer using the pixel buffer attributes specified during pool creation.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool)*