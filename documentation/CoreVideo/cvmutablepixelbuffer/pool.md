# CVMutablePixelBuffer.Pool

**Framework**: Core Video  
**Kind**: class

Manage and recycle pixel buffer backings.

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
final class Pool
```

## Topics

### Structures
- [CVMutablePixelBuffer.Pool.AllocationAttributes](cvmutablepixelbuffer/pool/allocationattributes.md)
  Controls how new pixel buffers are allocated when `CVMutablePixelBuffer/Pool/mutablePixelBuffer(with:)` is called.
- [CVMutablePixelBuffer.Pool.Configuration](cvmutablepixelbuffer/pool/configuration.md)
  Configuration passed to pixel buffer pool on creation.
### Initializers
- [init(pixelBufferAttributes: CVPixelBufferCreationAttributes, configuration: CVMutablePixelBuffer.Pool.Configuration) throws](cvmutablepixelbuffer/pool/init(pixelbufferattributes:configuration:).md)
  Create a new pixel buffer pool which creates pixel buffers using `pixelBufferAttributes`.
- [init(unsafePool: sending CVPixelBufferPool)](cvmutablepixelbuffer/pool/init(unsafepool:).md)
  Initialize a mutable pixel buffer pool by transferring existing CVPixelBufferPool.
### Instance Properties
- [var pixelBufferAttributes: CVPixelBufferCreationAttributes](cvmutablepixelbuffer/pool/pixelbufferattributes.md)
  Creation attributes for the pixel buffers created by this pool.
### Instance Methods
- [func flush(agedOutOnly: Bool)](cvmutablepixelbuffer/pool/flush(agedoutonly:).md)
  Frees as many buffers from the pool as possible.
- [func makeMutablePixelBuffer(CVMutablePixelBuffer.Pool.AllocationAttributes) throws -> CVMutablePixelBuffer](cvmutablepixelbuffer/pool/makemutablepixelbuffer(_:).md)
  This function creates a new CVMutablePixelBuffer using the pixel buffer attributes specified during pool creation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/pool)*