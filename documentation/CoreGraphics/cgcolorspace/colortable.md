# colorTable

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

The entries in the color table of an indexed color space.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var colorTable: [UInt8]? { get }
```

#### Discussion

If the color space is an indexed color space, this array contains color component values for the colors in the color space, in the same format you use when creating an indexed color space with the [`init(indexedBaseSpace:last:colorTable:)`](./init%28indexedbasespace,last,colortable%29.md) initializer.

If the color space is not an indexed color space, this property’s value is `nil`. To determine whether a color space is an indexed color space, read the [`model`](./model.md) property.

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
- [func copyICCData() -> CFData?](./copyiccdata%28%29.md)
  Returns a copy of the ICC profile data of the provided color space.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/colortable)*