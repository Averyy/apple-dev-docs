# NSColorSpace.Model

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the abstract model on which color space objects are based.

**Availability**:
- macOS

## Declaration

```swift
enum Model
```

```c
enum NSColorSpaceModel : NSInteger;
```

## Topics

### Color Spaces
- [NSColorSpace.Model.unknown](./model/unknown.md)
  An unknown color-space model.
- [NSColorSpace.Model.gray](./model/gray.md)
  The grayscale color-space model.
- [NSColorSpace.Model.rgb](./model/rgb.md)
  The RGB (red-green-blue) color-space model.
- [NSColorSpace.Model.cmyk](./model/cmyk.md)
  The CMYK (cyan-magenta-yellow-black) color-space model.
- [NSColorSpace.Model.lab](./model/lab.md)
  The L*a*b* device-independent color-space model, which represents colors relative to a reference white point.
- [NSColorSpace.Model.deviceN](./model/devicen.md)
  The DeviceN color-space model from Adobe Systems, Inc.
- [NSColorSpace.Model.indexed](./model/indexed.md)
  An indexed color space, which identifies discrete colors in a color list by index number.
- [NSColorSpace.Model.patterned](./model/patterned.md)
  A pattern color space, which is a repeated image that creates a tiled pattern.
### Deprecated
- [Deprecated symbols](../model-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Initializers
- [init?(rawValue: Int)](./model/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Color Space Data and Attributes
- [var cgColorSpace: CGColorSpace?](./cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](./colorspacemodel.md)
  The model on which the color space is based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](./colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](./iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var localizedName: String?](./localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](./numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace/model)*