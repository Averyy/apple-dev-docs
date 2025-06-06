# CVPlanarPixelBufferInfo_YCbCrBiPlanar

**Framework**: Core Video  
**Kind**: struct

A structure for describing YCbCr biplanar buffers.

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
struct CVPlanarPixelBufferInfo_YCbCrBiPlanar
```

## Topics

### Initializers
- [init()](cvplanarpixelbufferinfo_ycbcrbiplanar/init.md)
- [init(componentInfoY: CVPlanarComponentInfo, componentInfoCbCr: CVPlanarComponentInfo)](cvplanarpixelbufferinfo_ycbcrbiplanar/init(componentinfoy:componentinfocbcr:).md)
### Properties
- [var componentInfoCbCr: CVPlanarComponentInfo](cvplanarpixelbufferinfo_ycbcrbiplanar/componentinfocbcr.md)
  A [`CVPlanarComponentInfo`](cvplanarcomponentinfo.md) structure containing information on the Cb/Cr component of the buffer.
- [var componentInfoY: CVPlanarComponentInfo](cvplanarpixelbufferinfo_ycbcrbiplanar/componentinfoy.md)
  A [`CVPlanarComponentInfo`](cvplanarcomponentinfo.md) structure containing information on the Y component of the buffer.

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
- [struct CVPlanarPixelBufferInfo](cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvplanarpixelbufferinfo_ycbcrbiplanar)*