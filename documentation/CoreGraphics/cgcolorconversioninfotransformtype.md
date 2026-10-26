# CGColorConversionInfoTransformType

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Constants describing how a color conversion uses color spaces.

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
enum CGColorConversionInfoTransformType
```

```c
enum CGColorConversionInfoTransformType : uint32_t;
```

## Topics

### Enumeration Cases
- [CGColorConversionInfoTransformType.transformApplySpace](./cgcolorconversioninfotransformtype/transformapplyspace.md)
  Specifies a color conversion between one color profile and another.
- [CGColorConversionInfoTransformType.transformFromSpace](./cgcolorconversioninfotransformtype/transformfromspace.md)
  Specifies a color conversion from a device color space to a color profile.
- [CGColorConversionInfoTransformType.transformToSpace](./cgcolorconversioninfotransformtype/transformtospace.md)
  Specifies a color conversion from a color profile to a device color space.
### Initializers
- [init?(rawValue: UInt32)](./cgcolorconversioninfotransformtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./cgcolorconversioninfo/init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./cgcolorconversioninfo/init%28optionssrc,dst,options%29.md)
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype)*