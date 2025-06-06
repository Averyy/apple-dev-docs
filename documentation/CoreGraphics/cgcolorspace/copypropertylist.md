# copyPropertyList()

**Framework**: Core Graphics  
**Kind**: method

Returns a copy of the color space’s properties.

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
func copyPropertyList() -> CFPropertyList?
```

## See Also

- [init?(propertyListPlist: CFPropertyList)](cgcolorspace/init(propertylistplist:).md)
  Creates a color space from a property list.
- [var baseColorSpace: CGColorSpace?](cgcolorspace/basecolorspace.md)
  Returns the base color space of a pattern or indexed color space.
- [var numberOfComponents: Int](cgcolorspace/numberofcomponents.md)
  Returns the number of color components in a color space.
- [var model: CGColorSpaceModel](cgcolorspace/model.md)
  Returns the color space model of the provided color space.
- [enum CGColorSpaceModel](cgcolorspacemodel.md)
  Models for color spaces.
- [var colorTable: [UInt8]?](cgcolorspace/colortable.md)
  The entries in the color table of an indexed color space.
- [func copyICCData() -> CFData?](cgcolorspace/copyiccdata.md)
  Returns a copy of the ICC profile data of the provided color space.
- [var iccData: CFData?](cgcolorspace/iccdata.md)
  Returns a copy of the ICC profile of the provided color space.
- [var name: CFString?](cgcolorspace/name.md)
  Returns the name used to create the specified color space.
- [var supportsOutput: Bool](cgcolorspace/supportsoutput.md)
  Returns a Boolean indicating whether the color space can be used as a destination color space.
- [var isWideGamutRGB: Bool](cgcolorspace/iswidegamutrgb.md)
  Returns whether the RGB color space covers a significant portion of the NTSC color gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/copypropertylist())*