# CGColorConversionInfo

**Framework**: Core Graphics  
**Kind**: class  
**Role**: Class

An object that describes how to convert between color spaces for use by other system services.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class CGColorConversionInfo
```

```c
typedef const struct CGColorConversionInfo * CGColorConversionInfoRef;
```

#### Overview

A [`CGColorConversionInfo`](./cgcolorconversioninfo.md) object specifies a conversion between two or more color spaces, including information about the intent of the conversion. You use color conversion objects to specify the work to be done by an [`MPSImageConversion`](../MetalPerformanceShaders/mpsimageconversion.md) filter, which can then perform GPU-accelerated image conversion.

## Topics

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./cgcolorconversioninfo/init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./cgcolorconversioninfo/init%28optionssrc,dst,options%29.md)
- [enum CGColorConversionInfoTransformType](./cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](./cgcolorconversioninfo/typeid.md)
  Returns the Core Foundation type identifier for a color conversion info data type.
### Instance Methods
- [func convert(width: Int, height: Int, to: UnsafeMutableRawPointer, format: CGColorBufferFormat, from: UnsafeRawPointer, format: CGColorBufferFormat, options: CFDictionary?) -> Bool](./cgcolorconversioninfo/convert%28width,height,to,format,from,format,options%29.md)
### Initializers
- [init?(src: CGColorSpace, srcHeadroom: Float, dst: CGColorSpace, dstHeadroom: Float, toneMapping: CGToneMapping, options: CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](./cgcolorconversioninfo/init%28src,srcheadroom,dst,dstheadroom,tonemapping,options,_%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Colors and Fonts
- [class CGColor](./cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorSpace](./cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [class CGFont](./cgfont.md)
  A set of character glyphs and layout information for drawing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo)*