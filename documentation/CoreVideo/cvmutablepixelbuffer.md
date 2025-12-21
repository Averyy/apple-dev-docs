# CVMutablePixelBuffer

**Framework**: Core Video  
**Kind**: struct

CVMutablePixelBuffer provides read-write access to the pixel data and attachments.

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
struct CVMutablePixelBuffer
```

## Topics

### Classes
- [CVMutablePixelBuffer.Pool](cvmutablepixelbuffer/pool.md)
  Manage and recycle pixel buffer backings.
### Initializers
- [init(CVPixelBufferCreationAttributes) throws](cvmutablepixelbuffer/init(_:).md)
  Creates a CVPixelBuffer with given attributes. It allocates the necessary memory based on the dimensions, pixel format and extended pixels described in the `CVPixelBuffer/Attributes`.
- [init(unsafeBacking: IOSurface, matching: CVPixelBufferCreationAttributes) throws](cvmutablepixelbuffer/init(unsafebacking:matching:).md)
  Creates a CVPixelBuffer backed by the given `ioSurface`. The CVPixelBuffer will retain the `ioSurface`.  If you are using IOSurface to share CVPixelBuffers between processes and those CVPixelBuffers are allocated via a CVPixelBufferPool, it is important that the CVPixelBufferPool does not reuse CVPixelBuffers whose IOSurfaces are still in use in other processes. CoreVideo and IOSurface will take care of this for if you use IOSurfaceCreateMachPort and IOSurfaceLookupFromMachPort, but NOT if you pass IOSurfaceIDs.
- [init(unsafeBuffer: sending CVPixelBuffer)](cvmutablepixelbuffer/init(unsafebuffer:).md)
  Initialize a mutable pixel buffer by transferring existing CVPixelBuffer value.
### Instance Methods
- [func accessUnsafeMutableRawPlaneBytes<R>(([(properties: CVPixelBufferPlaneProperties, bytes: UnsafeMutableRawBufferPointer)]) throws -> sending R) rethrows -> sending R](cvmutablepixelbuffer/accessunsafemutablerawplanebytes(_:).md)
  Access the pixels in the planes contained within this buffer. The base address is locked for writing during the execution of the block.
- [func fillExtendedPixels() -> Bool](cvmutablepixelbuffer/fillextendedpixels.md)
  Fills the extended pixels of the pixel buffer. This method replicates the edge pixels to fill the entire extended region of the image.
- [func withUnsafeBuffer<R>((CVPixelBuffer) throws -> sending R) rethrows -> sending R](cvmutablepixelbuffer/withunsafebuffer(_:).md)

## Relationships

### Conforms To
- [CVBufferRepresentable](cvbufferrepresentable.md)
- [CVImageBufferRepresentable](cvimagebufferrepresentable.md)
- [CVPixelBufferRepresentable](cvpixelbufferrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer)*