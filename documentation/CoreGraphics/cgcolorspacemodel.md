# CGColorSpaceModel

**Framework**: Core Graphics  
**Kind**: enum  
**Role**: Enumeration

Models for color spaces.

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
enum CGColorSpaceModel
```

```c
enum CGColorSpaceModel : int32_t;
```

## Topics

### Constants
- [CGColorSpaceModel.unknown](./cgcolorspacemodel/unknown.md)
  An unknown color space model.
- [CGColorSpaceModel.monochrome](./cgcolorspacemodel/monochrome.md)
  A monochrome color space model.
- [CGColorSpaceModel.rgb](./cgcolorspacemodel/rgb.md)
  An RGB color space model.
- [CGColorSpaceModel.cmyk](./cgcolorspacemodel/cmyk.md)
  A CMYK color space model.
- [CGColorSpaceModel.lab](./cgcolorspacemodel/lab.md)
  A Lab color space model.
- [CGColorSpaceModel.deviceN](./cgcolorspacemodel/devicen.md)
  A DeviceN color space model.
- [CGColorSpaceModel.indexed](./cgcolorspacemodel/indexed.md)
  An indexed color space model.
- [CGColorSpaceModel.pattern](./cgcolorspacemodel/pattern.md)
  A pattern color space model.
- [CGColorSpaceModel.XYZ](./cgcolorspacemodel/xyz.md)
  An XYZ color space model.
### Initializers
- [init?(rawValue: Int32)](./cgcolorspacemodel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Examining a Color Space
- [var baseColorSpace: CGColorSpace?](./cgcolorspace/basecolorspace.md)
  Returns the base color space of a pattern or indexed color space.
- [var numberOfComponents: Int](./cgcolorspace/numberofcomponents.md)
  Returns the number of color components in a color space.
- [var model: CGColorSpaceModel](./cgcolorspace/model.md)
  Returns the color space model of the provided color space.
- [var colorTable: [UInt8]?](./cgcolorspace/colortable.md)
  The entries in the color table of an indexed color space.
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
- [CGColorSpaceGetColorTableCount](./cgcolorspacegetcolortablecount.md)
  Returns the number of entries in the color table of an indexed color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel)*