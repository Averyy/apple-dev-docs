# init(optionsSrc:dst:options:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.14.6+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init?(optionsSrc src: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)
```

```c
extern CGColorConversionInfoRefCGColorConversionInfoCreateWithOptions(CGColorSpaceRef src, CGColorSpaceRef dst, CFDictionaryRef options);
```

## See Also

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [enum CGColorConversionInfoTransformType](../cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(optionssrc:dst:options:))*