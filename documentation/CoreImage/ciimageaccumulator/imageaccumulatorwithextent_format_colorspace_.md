# imageAccumulatorWithExtent:format:colorSpace:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates an image accumulator with the specified extent, pixel format, and color space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) imageAccumulatorWithExtent:(CGRect) extent format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace;
```

#### Return Value

The image accumulator object.

## Parameters

- `extent`: A rectangle that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.
- `format`: The format and size of each pixel. You must supply a pixel format constant, such as  kCIFormatARGB8  (32 bit-per-pixel, fixed-point pixel format) or kCIFormatRGBAf (128 bit-per-pixel, floating-point pixel format). See [`CIImage`](../ciimage.md) for more information about pixel format constants.
- `colorSpace`: A [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) object describing the color space for the image accumulator.

## See Also

### Related Documentation
- [init?(extent: CGRect, format: CIFormat)](./init%28extent,format%29.md)
  Initializes an image accumulator with the specified extent and pixel format.
### Creating an Image Accumulator
- [+ imageAccumulatorWithExtent:format:](./imageaccumulatorwithextent_format_.md)
  Creates an image accumulator with the specified extent and pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/imageaccumulatorwithextent:format:colorspace:)*