# CVPixelBuffer

**Framework**: Core Video  
**Kind**: typealias

A reference to a Core Video pixel buffer object.

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
typealias CVPixelBuffer = CVImageBuffer
```

#### Discussion

The pixel buffer stores an image in main memory.

## See Also

- [struct CVPixelBufferLockFlags](cvpixelbufferlockflags.md)
  The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md).
- [struct CVPlanarComponentInfo](cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo](cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffer)*