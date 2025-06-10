# vImageAffineWarp_ARGB16F(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImageAffineWarp_ARGB16F(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ transform: UnsafePointer<vImage_AffineTransform>, _ backColor: UnsafePointer<UInt16>!, _ flags: vImage_Flags) -> vImage_Error
```

## See Also

- [func vImageAffineWarp_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_8, vImage_Flags) -> vImage_Error](vimageaffinewarp_planar8(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an 8-bit planar image.
- [func vImageAffineWarp_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_F, vImage_Flags) -> vImage_Error](vimageaffinewarp_planarf(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a 32-bit planar image.
- [func vImageAffineWarp_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb16u(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an unsigned 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<Int16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb16s(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a signed 16-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argb8888(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to an 8-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_argbffff(_:_:_:_:_:_:).md)
  Applies a single-precision affine transformation to a 32-bit-per-channel, 4-channel interleaved image.
- [func vImageAffineWarp_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimageaffinewarp_cbcr16f(_:_:_:_:_:_:).md)
- [func vImageAffineWarp_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImage_AffineTransform>, Pixel_16F, vImage_Flags) -> vImage_Error](vimageaffinewarp_planar16f(_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageaffinewarp_argb16f(_:_:_:_:_:_:))*