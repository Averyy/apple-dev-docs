# init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:_:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

> **Deprecated**: declared Swift name 'init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:)' was adjusted to 'init(src:srcHeadroom:dst:dstHeadroom:toneMapping:options:_:)' because it does not have the correct number of parameters (6 vs. 7); please report this to its maintainer

## Declaration

```swift
init?(src source: CGColorSpace, srcHeadroom source_headroom: Float, dst target: CGColorSpace, dstHeadroom target_headroom: Float, toneMapping method: CGToneMapping, options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

```c
extern CGColorConversionInfoRefCGColorConversionInfoCreateForToneMapping(CGColorSpaceRef source, float source_headroom, CGColorSpaceRef target, float target_headroom, CGToneMapping method, CFDictionaryRef options, CFErrorRef*error);
```

## See Also

### Creating a Color Conversion
- [init?(src: CGColorSpace, dst: CGColorSpace)](./init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./init%28optionssrc,dst,options%29.md)
- [enum CGColorConversionInfoTransformType](../cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [CGColorConversionInfoCreateFromList](../cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:_:))*