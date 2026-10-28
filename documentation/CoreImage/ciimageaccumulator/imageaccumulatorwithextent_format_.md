# imageAccumulatorWithExtent:format:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates an image accumulator with the specified extent and pixel format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) imageAccumulatorWithExtent:(CGRect) extent format:(CIFormat) format;
```

## Return Value

The image accumulator object.

## Parameters

- `extent`: A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.
- `format`: The format and size of each pixel. You must supply a pixel format constant, such as  kCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [`CIImage`](../ciimage.md) for more information about pixel format constants.

## See Also

### Related Documentation
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [init?(extent: CGRect, format: CIFormat)](./init%28extent,format%29.md)
  Initializes an image accumulator with the specified extent and pixel format.
### Creating an Image Accumulator
- [+ imageAccumulatorWithExtent:format:colorSpace:](./imageaccumulatorwithextent_format_colorspace_.md)
  Creates an image accumulator with the specified extent, pixel format, and color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:)*