# CGColorConversionInfoTransformType

**Framework**: Core Graphics  
**Kind**: enum

Constants describing how a color conversion uses color spaces.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CGColorConversionInfoTransformType
```

## Topics

### Enumeration Cases
- [CGColorConversionInfoTransformType.transformApplySpace](cgcolorconversioninfotransformtype/transformapplyspace.md)
  Specifies a color conversion between one color profile and another.
- [CGColorConversionInfoTransformType.transformFromSpace](cgcolorconversioninfotransformtype/transformfromspace.md)
  Specifies a color conversion from a device color space to a color profile.
- [CGColorConversionInfoTransformType.transformToSpace](cgcolorconversioninfotransformtype/transformtospace.md)
  Specifies a color conversion from a color profile to a device color space.
### Initializers
- [init?(rawValue: UInt32)](cgcolorconversioninfotransformtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(src: CGColorSpace, dst: CGColorSpace)](cgcolorconversioninfo/init(src:dst:).md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](cgcolorconversioninfo/init(optionssrc:dst:options:).md)
- [init?(src: CGColorSpace, srcHeadroom: Float, dst: CGColorSpace, dstHeadroom: Float, toneMapping: CGToneMapping, options: CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype)*