# shear(direction:translate:slope:resamplingFilter:backgroundColor:useFloat16Accumulator:destination:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, two-channel interleaved pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F16F? = (0, 0), useFloat16Accumulator: Bool = false, destination: vImage.PixelBuffer<Format>) where T : BinaryFloatingPoint
```

Available when `Format` is `vImage.Interleaved16Fx2`.

## Parameters

- `direction`: An enumeration that specifies the shear direction.
- `translate`: A value that specifies the translation.
- `slope`: The slope of the front edge of the sheared image.
- `resamplingFilter`: The resampling filter that the function uses. For more information, see [Reducing artifacts with custom resampling filters](../../reducing-artifacts-with-custom-resampling-filters.md).
- `backgroundColor`: An optional background color. If you pass `nil`, the operation uses the [`kvImageEdgeExtend`](../../kvimageedgeextend.md) flag to extend the edges of the image infinitely.
- `useFloat16Accumulator`: A Boolean value that specifies that the function uses faster, but lower-precision, internal arithmetic. For more information, see [`kvImageUseFP16Accumulator`](../../kvimageusefp16accumulator.md).
- `destination`: The destination pixel buffer.

## See Also

### Related Documentation
- [Applying geometric transforms to images](../../applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
### Shearing images
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-2gf4y.md)
  Performs a horizontal or vertical shear operation on an 8-bit planar pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-5busu.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,usefloat16accumulator,destination%29-26sh4.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_F?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-85o1n.md)
  Performs a horizontal or vertical shear operation on a 32-bit planar pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_16U16U?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-57dzf.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear(direction: vImage.ShearDirection, translate: Float, slope: Float, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_88?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-7fou8.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, two-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_8888?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-95446.md)
  Performs a horizontal or vertical shear operation on an 8-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16U?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-2ezuh.md)
  Performs a horizontal or vertical shear operation on an unsigned 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_ARGB_16F?, useFloat16Accumulator: Bool, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,usefloat16accumulator,destination%29-7kddt.md)
  Performs a horizontal or vertical shear operation on a floating-point 16-bit-per-channel, four-channel interleaved pixel buffer.
- [func shear<T>(direction: vImage.ShearDirection, translate: T, slope: T, resamplingFilter: ResamplingFilter, backgroundColor: Pixel_FFFF?, destination: vImage.PixelBuffer<Format>)](./shear%28direction,translate,slope,resamplingfilter,backgroundcolor,destination%29-7r29q.md)
  Performs a horizontal or vertical shear operation on a 32-bit-per-channel, four-channel interleaved pixel buffer.
- [vImage.ShearDirection](../sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/shear(direction:translate:slope:resamplingfilter:backgroundcolor:usefloat16accumulator:destination:)-7nh4n)*