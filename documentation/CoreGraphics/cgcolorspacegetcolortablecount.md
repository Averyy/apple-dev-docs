# CGColorSpaceGetColorTableCount

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the number of entries in the color table of an indexed color space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern size_t CGColorSpaceGetColorTableCount(CGColorSpaceRef space);
```

## Return Value

The number of entries in the color table of the `space` parameter if the color space is an indexed color space; otherwise, returns `0`.

## Parameters

- `space`: A color space object for an indexed color space.

## See Also

### Examining a Color Space
- [var baseColorSpace: CGColorSpace?](./cgcolorspace/basecolorspace.md)
  Returns the base color space of a pattern or indexed color space.
- [var numberOfComponents: Int](./cgcolorspace/numberofcomponents.md)
  Returns the number of color components in a color space.
- [var model: CGColorSpaceModel](./cgcolorspace/model.md)
  Returns the color space model of the provided color space.
- [enum CGColorSpaceModel](./cgcolorspacemodel.md)
  Models for color spaces.
- [func copyICCData() -> CFData?](./cgcolorspace/copyiccdata%28%29.md)
  Returns a copy of the ICC profile data of the provided color space.
- [func copyPropertyList() -> CFPropertyList?](./cgcolorspace/copypropertylist%28%29.md)
  Returns a copy of the color space’s properties.
- [var iccData: CFData?](./cgcolorspace/iccdata.md)
  Returns a copy of the ICC profile of the provided color space.
- [var name: CFString?](./cgcolorspace/name.md)
  Returns the name used to create the specified color space.
- [var supportsOutput: Bool](./cgcolorspace/supportsoutput.md)
  Returns a Boolean indicating whether the color space can be used as a destination color space.
- [var isWideGamutRGB: Bool](./cgcolorspace/iswidegamutrgb.md)
  Returns whether the RGB color space covers a significant portion of the NTSC color gamut.
- [CGColorSpaceGetColorTable](./cgcolorspacegetcolortable.md)
  Copies the entries in the color table of an indexed color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspacegetcolortablecount)*