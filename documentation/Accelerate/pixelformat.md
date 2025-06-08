# PixelFormat

**Framework**: Accelerate  
**Kind**: protocol

A pixel buffer pixel format.

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
protocol PixelFormat
```

## Topics

### Associated Types
- [associatedtype ComponentType : Equatable](pixelformat/componenttype.md)
  The type of the pixel’s component.

## Relationships

### Inherited By
- [InitializableFromCGImage](initializablefromcgimage.md)
- [MultiplePlanePixelFormat](multipleplanepixelformat.md)
- [SinglePlanePixelFormat](singleplanepixelformat.md)
- [StaticPixelFormat](staticpixelformat.md)
### Conforming Types
- [vImage.DynamicPixelFormat](vimage/dynamicpixelformat.md)
- [vImage.Interleaved16Fx2](vimage/interleaved16fx2.md)
- [vImage.Interleaved16Fx4](vimage/interleaved16fx4.md)
- [vImage.Interleaved16Ux2](vimage/interleaved16ux2.md)
- [vImage.Interleaved16Ux4](vimage/interleaved16ux4.md)
- [vImage.Interleaved8x2](vimage/interleaved8x2.md)
- [vImage.Interleaved8x3](vimage/interleaved8x3.md)
- [vImage.Interleaved8x4](vimage/interleaved8x4.md)
- [vImage.InterleavedFx2](vimage/interleavedfx2.md)
- [vImage.InterleavedFx3](vimage/interleavedfx3.md)
- [vImage.InterleavedFx4](vimage/interleavedfx4.md)
- [vImage.Planar16F](vimage/planar16f.md)
- [vImage.Planar16U](vimage/planar16u.md)
- [vImage.Planar8](vimage/planar8.md)
- [vImage.Planar8x2](vimage/planar8x2.md)
- [vImage.Planar8x3](vimage/planar8x3.md)
- [vImage.Planar8x4](vimage/planar8x4.md)
- [vImage.PlanarF](vimage/planarf.md)
- [vImage.PlanarFx2](vimage/planarfx2.md)
- [vImage.PlanarFx3](vimage/planarfx3.md)
- [vImage.PlanarFx4](vimage/planarfx4.md)

## See Also

- [protocol StaticPixelFormat](staticpixelformat.md)
  A pixel format that’s known at compile time.
- [protocol InitializableFromCGImage](initializablefromcgimage.md)
  A pixel format that supports initialization from a Core Graphics image.
- [protocol SinglePlanePixelFormat](singleplanepixelformat.md)
  A pixel format that contains a single underlying vImage buffer.
- [protocol MultiplePlanePixelFormat](multipleplanepixelformat.md)
  A pixel format that contains multiple homogeneous planes represented by multiple underlying vImage buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/pixelformat)*