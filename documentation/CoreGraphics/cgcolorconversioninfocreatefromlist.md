# CGColorConversionInfoCreateFromList

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Creates a conversion between an arbitrary number of specified color spaces.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern CGColorConversionInfoRefCGColorConversionInfoCreateFromList(CFDictionaryRef options, CGColorSpaceRef , CGColorConversionInfoTransformType , CGColorRenderingIntent , ...);
```

##### Parameters

- **options**: A dictionary containing options for color space conversion. See [`CGColorConversionInfo`](./cgcolorconversioninfo.md).
- **colorSpace**: The first color space in the conversion.
- **transformType**: The role of the first color space to the conversion process. See [`CGColorConversionInfoTransformType`](./cgcolorconversioninfotransformtype.md).
- **renderingIntent**: The rendering intent to use with the first color space. See [`CGColorRenderingIntent`](./cgcolorrenderingintent.md).
- **…**: A `NULL`-terminated list of additional `colorSpace, transformType, renderingIntent` triplets.

##### Returns

A color conversion object, or `nil` if no conversion between the specified color spaces is allowed.

#### Discussion

To call this function you must pass a triplet of color space, transform type, and rendering intent for each color space in the chain of conversions. For example, the following code is equivalent to calling [`init(src:dst:)`](./cgcolorconversioninfo/init%28src,dst%29.md):

```objc
// convert from `src` to `dst` space with default intent
CGColorConversionInfoCreateFromList(NULL,
    src, kCGColorConversionTransformFromSpace, kCGRenderingIntentDefault,
    dst, kCGColorConversionTransformToSpace,   kCGRenderingIntentDefault,
    NULL);
```

To extend this example to convert through an intermediate color space, insert another space/type/intent triplet between the `src` and `dst` lines, using the [`CGColorConversionInfoTransformType.transformApplySpace`](./cgcolorconversioninfotransformtype/transformapplyspace.md) type.

The listed color spaces must be calibrated color spaces (that is, not device-specific or indexed color spaces), and the list must contain at least two color spaces (that is, two triplets of space, type, and intent).

You can use a color conversion object to create [`MPSImageConversion`](../MetalPerformanceShaders/mpsimageconversion.md) filters that perform GPU-accelerated color space conversion.

## See Also

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./cgcolorconversioninfo/init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./cgcolorconversioninfo/init%28optionssrc,dst,options%29.md)
- [enum CGColorConversionInfoTransformType](./cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfocreatefromlist)*