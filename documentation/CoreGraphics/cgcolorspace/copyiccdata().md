# copyICCData()

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Returns a copy of the ICC profile data of the provided color space.

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
func copyICCData() -> CFData?
```

```c
extern CFDataRefCGColorSpaceCopyICCData(CGColorSpaceRef space);
```

## Return Value

The ICC profile data or `NULL` if the color space does not have an ICC data profile.

## See Also

### Examining a Color Space
- [var baseColorSpace: CGColorSpace?](./basecolorspace.md)
  Returns the base color space of a pattern or indexed color space.
- [var numberOfComponents: Int](./numberofcomponents.md)
  Returns the number of color components in a color space.
- [var model: CGColorSpaceModel](./model.md)
  Returns the color space model of the provided color space.
- [enum CGColorSpaceModel](../cgcolorspacemodel.md)
  Models for color spaces.
- [var colorTable: [UInt8]?](./colortable.md)
  The entries in the color table of an indexed color space.
- [func copyPropertyList() -> CFPropertyList?](./copypropertylist%28%29.md)
  Returns a copy of the color space’s properties.
- [var iccData: CFData?](./iccdata.md)
  Returns a copy of the ICC profile of the provided color space.
- [var name: CFString?](./name.md)
  Returns the name used to create the specified color space.
- [var supportsOutput: Bool](./supportsoutput.md)
  Returns a Boolean indicating whether the color space can be used as a destination color space.
- [var isWideGamutRGB: Bool](./iswidegamutrgb.md)
  Returns whether the RGB color space covers a significant portion of the NTSC color gamut.
- [CGColorSpaceGetColorTable](../cgcolorspacegetcolortable.md)
  Copies the entries in the color table of an indexed color space.
- [CGColorSpaceGetColorTableCount](../cgcolorspacegetcolortablecount.md)
  Returns the number of entries in the color table of an indexed color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/copyiccdata())*