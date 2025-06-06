# CVPlanarPixelBufferInfo

**Framework**: Core Video  
**Kind**: struct

A structure for describing planar buffers.

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
struct CVPlanarPixelBufferInfo
```

## Topics

### Initializers
- [init()](cvplanarpixelbufferinfo/init.md)
- [init(componentInfo: CVPlanarComponentInfo)](cvplanarpixelbufferinfo/init(componentinfo:).md)
### Properties
- [var componentInfo: CVPlanarComponentInfo](cvplanarpixelbufferinfo/componentinfo.md)
  An array containing a [`CVPlanarComponentInfo`](cvplanarcomponentinfo.md) structure for each plane of the buffer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CVPixelBuffer](cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPixelBufferLockFlags](cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md).
- [struct CVPlanarComponentInfo](cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvplanarpixelbufferinfo)*