# CVPlanarPixelBufferInfo_YCbCrPlanar

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

A structure for describing YCbCr planar buffers.

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
struct CVPlanarPixelBufferInfo_YCbCrPlanar
```

```c
struct CVPlanarPixelBufferInfo_YCbCrPlanar;
```

## Topics

### Initializers
- [init()](./cvplanarpixelbufferinfo_ycbcrplanar/init%28%29.md)
- [init(componentInfoY: CVPlanarComponentInfo, componentInfoCb: CVPlanarComponentInfo, componentInfoCr: CVPlanarComponentInfo)](./cvplanarpixelbufferinfo_ycbcrplanar/init%28componentinfoy,componentinfocb,componentinfocr%29.md)
### Properties
- [var componentInfoCb: CVPlanarComponentInfo](./cvplanarpixelbufferinfo_ycbcrplanar/componentinfocb.md)
  A [`CVPlanarComponentInfo`](./cvplanarcomponentinfo.md) structure containing information on the Cb component of the buffer.
- [var componentInfoCr: CVPlanarComponentInfo](./cvplanarpixelbufferinfo_ycbcrplanar/componentinfocr.md)
  A [`CVPlanarComponentInfo`](./cvplanarcomponentinfo.md) structure containing information on the Cr component of the buffer.
- [var componentInfoY: CVPlanarComponentInfo](./cvplanarpixelbufferinfo_ycbcrplanar/componentinfoy.md)
  A [`CVPlanarComponentInfo`](./cvplanarcomponentinfo.md) structure containing information on the Y component of the buffer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [typealias CVPixelBuffer](./cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPixelBufferLockFlags](./cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](./cvpixelbufferlockbaseaddress%28_,_%29.md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](./cvpixelbufferunlockbaseaddress%28_,_%29.md).
- [struct CVPlanarComponentInfo](./cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo](./cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](./cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvplanarpixelbufferinfo_ycbcrplanar)*