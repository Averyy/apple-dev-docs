# CVPlanarComponentInfo

**Framework**: Core Video  
**Kind**: struct

A structure for describing planar components.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CVPlanarComponentInfo
```

#### Overview

Depending on how they were created, planar pixel buffers may or may not have this descriptor at their base address. For this reason, you should use [`CVPixelBufferGetBaseAddressOfPlane(_:_:)`](cvpixelbuffergetbaseaddressofplane(_:_:).md) and [`CVPixelBufferGetBytesPerRowOfPlane(_:_:)`](cvpixelbuffergetbytesperrowofplane(_:_:).md) to get information about a planar pixel buffer.

## Topics

### Initializers
- [init()](cvplanarcomponentinfo/init.md)
- [init(offset: Int32, rowBytes: UInt32)](cvplanarcomponentinfo/init(offset:rowbytes:).md)
### Properties
- [var offset: Int32](cvplanarcomponentinfo/offset.md)
  The offset from the main base address to the base address of this plane. (big-endian)
- [var rowBytes: UInt32](cvplanarcomponentinfo/rowbytes.md)
  The number of bytes per row of this plane. (big-endian)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CVPixelBuffer](cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPixelBufferLockFlags](cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md).
- [struct CVPlanarPixelBufferInfo](cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvplanarcomponentinfo)*