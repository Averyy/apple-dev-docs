# init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:)

**Framework**: Core Graphics  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init?(src from: CGColorSpace, srcHeadroom source_headroom: Float, dst to: CGColorSpace, dstHeadroom target_headroom: Float, toneMapping method: CGToneMapping, options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

## See Also

- [init?(src: CGColorSpace, dst: CGColorSpace)](cgcolorconversioninfo/init(src:dst:).md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](cgcolorconversioninfo/init(optionssrc:dst:options:).md)
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:))*