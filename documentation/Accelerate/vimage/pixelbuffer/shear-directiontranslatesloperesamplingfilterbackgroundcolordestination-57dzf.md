# shear(direction:translate:slope:resamplingFilter:backgroundColor:destination:)

**Framework**: Accelerate  
**Kind**: method

Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer.

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
func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U16U? = (0, 0), destination: vImage.PixelBuffer<Format>) where T : BinaryFloatingPoint
```

## Parameters

- `direction`: An enumeration that specifies the shear direction.
- `translate`: A value that specifies the translation.
- `slope`: The slope of the front edge of the sheared image.
- `resamplingFilter`: The resampling filter that the function uses. For more information, see  .
- `backgroundColor`: An optional background color. If you pass  , the operation uses the   flag to extend the edges of the image infinitely.
- `destination`: The destination pixel buffer.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-2gf4y.md)
  Performs a horizontal or vertical shear operation on an 8-bit planar pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-5busu.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-26sh4.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-85o1n.md)
  Performs a horizontal or vertical shear operation on a 32-bit planar pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_88?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-7fou8.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-7nh4n.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-95446.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-2ezuh.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-7kddt.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-7r29q.md)
  Performs a horizontal or vertical shear operation on a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:destination:)-57dzf)*