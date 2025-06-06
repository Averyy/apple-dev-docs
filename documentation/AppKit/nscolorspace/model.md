# NSColorSpace.Model

**Framework**: AppKit  
**Kind**: enum

Constants that describe the abstract model on which color space objects are based.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Model
```

## Topics

### Color Spaces
- [NSColorSpace.Model.unknown](nscolorspace/model/unknown.md)
  An unknown color-space model.
- [NSColorSpace.Model.gray](nscolorspace/model/gray.md)
  The grayscale color-space model.
- [NSColorSpace.Model.rgb](nscolorspace/model/rgb.md)
  The RGB (red-green-blue) color-space model.
- [NSColorSpace.Model.cmyk](nscolorspace/model/cmyk.md)
  The CMYK (cyan-magenta-yellow-black) color-space model.
- [NSColorSpace.Model.lab](nscolorspace/model/lab.md)
  The L*a*b* device-independent color-space model, which represents colors relative to a reference white point.
- [NSColorSpace.Model.deviceN](nscolorspace/model/devicen.md)
  The DeviceN color-space model from Adobe Systems, Inc.
- [NSColorSpace.Model.indexed](nscolorspace/model/indexed.md)
  An indexed color space, which identifies discrete colors in a color list by index number.
- [NSColorSpace.Model.patterned](nscolorspace/model/patterned.md)
  A pattern color space, which is a repeated image that creates a tiled pattern.
### Initializers
- [init?(rawValue: Int)](nscolorspace/model/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var cgColorSpace: CGColorSpace?](nscolorspace/cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](nscolorspace/colorspacemodel.md)
  The model on which the color space is based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](nscolorspace/colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](nscolorspace/iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var localizedName: String?](nscolorspace/localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](nscolorspace/numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/model)*