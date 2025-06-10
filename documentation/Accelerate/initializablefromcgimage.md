# InitializableFromCGImage

**Framework**: Accelerate  
**Kind**: protocol

A pixel format that supports initialization from a Core Graphics image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol InitializableFromCGImage : SinglePlanePixelFormat
```

## Topics

### Type Properties
- [static var bitCountPerComponent: Int](initializablefromcgimage/bitcountpercomponent.md)
  The number of bits in a channel.

## Relationships

### Inherits From
- [PixelFormat](pixelformat.md)
- [SinglePlanePixelFormat](singleplanepixelformat.md)
### Conforming Types
- [vImage.Interleaved16Fx4](vimage/interleaved16fx4.md)
- [vImage.Interleaved16Ux2](vimage/interleaved16ux2.md)
- [vImage.Interleaved16Ux4](vimage/interleaved16ux4.md)
- [vImage.Interleaved8x3](vimage/interleaved8x3.md)
- [vImage.Interleaved8x4](vimage/interleaved8x4.md)
- [vImage.InterleavedFx3](vimage/interleavedfx3.md)
- [vImage.InterleavedFx4](vimage/interleavedfx4.md)
- [vImage.Planar16F](vimage/planar16f.md)
- [vImage.Planar8](vimage/planar8.md)
- [vImage.PlanarF](vimage/planarf.md)

## See Also

- [protocol MultiplePlanePixelFormat](multipleplanepixelformat.md)
  A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.
- [protocol PixelFormat](pixelformat.md)
  A pixel buffer pixel format.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/initializablefromcgimage)*