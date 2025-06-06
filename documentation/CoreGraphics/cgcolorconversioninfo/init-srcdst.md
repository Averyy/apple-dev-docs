# init(src:dst:)

**Framework**: Core Graphics  
**Kind**: init

Creates a conversion between two specified color spaces.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init?(src: CGColorSpace, dst: CGColorSpace)
```

#### Return Value

A color conversion object, or `nil` if no conversion between the specified color spaces is allowed.

#### Discussion

The source and destination color spaces must be calibrated color spaces (that is, not device-specific or indexed color spaces).

You can use a color conversion object to create [`MPSImageConversion`](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion) filters that perform GPU-accelerated color space conversion.

## Parameters

- `src`: The source color space from which color values are to be converted.
- `dst`: The destination color space to which colors are to be converted.

## See Also

- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](cgcolorconversioninfo/init(optionssrc:dst:options:).md)
- [init?(src: CGColorSpace, srcHeadroom: Float, dst: CGColorSpace, dstHeadroom: Float, toneMapping: CGToneMapping, options: CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:).md)
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo/init(src:dst:))*