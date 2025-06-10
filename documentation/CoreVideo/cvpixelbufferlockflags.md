# CVPixelBufferLockFlags

**Framework**: Core Video  
**Kind**: struct

The flags to pass to [`CVPixelBufferLockBaseAddress(_:_:)`](cvpixelbufferlockbaseaddress(_:_:).md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](cvpixelbufferunlockbaseaddress(_:_:).md).

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
struct CVPixelBufferLockFlags
```

## Topics

### Constants
- [static var readOnly: CVPixelBufferLockFlags](cvpixelbufferlockflags/readonly.md)
  A read-only buffer.
### Initializers
- [init(rawValue: CVOptionFlags)](cvpixelbufferlockflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias CVPixelBuffer](cvpixelbuffer.md)
  A reference to a Core Video pixel buffer object.
- [struct CVPlanarComponentInfo](cvplanarcomponentinfo.md)
  A structure for describing planar components.
- [struct CVPlanarPixelBufferInfo](cvplanarpixelbufferinfo.md)
  A structure for describing planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrPlanar](cvplanarpixelbufferinfo_ycbcrplanar.md)
  A structure for describing YCbCr planar buffers.
- [struct CVPlanarPixelBufferInfo_YCbCrBiPlanar](cvplanarpixelbufferinfo_ycbcrbiplanar.md)
  A structure for describing YCbCr biplanar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferlockflags)*