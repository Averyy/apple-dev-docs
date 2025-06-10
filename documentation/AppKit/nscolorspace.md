# NSColorSpace

**Framework**: AppKit  
**Kind**: class

An object that represents a custom color space.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSColorSpace
```

#### Overview

You can make custom color spaces from ColorSync profiles or from ICC profiles. [`NSColorSpace`](nscolorspace.md) also has factory methods that return objects representing the system color spaces.

You can use the [`init(colorSpace:components:count:)`](nscolor/init(colorspace:components:count:).md) method of the [`NSColor`](nscolor.md) class to create color objects using custom [`NSColorSpace`](nscolorspace.md) objects. You can also send the [`usingColorSpace(_:)`](nscolor/usingcolorspace(_:).md) message to an [`NSColor`](nscolor.md) object to convert it between two color spaces, either of which may be a custom color space.

## Topics

### Getting a Named Color Space
- [class var deviceRGB: NSColorSpace](nscolorspace/devicergb.md)
  A color space object that represents a calibrated or device-dependent RGB color space.
- [class var genericRGB: NSColorSpace](nscolorspace/genericrgb.md)
  A color space object that represents a device-independent RGB color space.
- [class var deviceCMYK: NSColorSpace](nscolorspace/devicecmyk.md)
  A color space object that represents a calibrated or device-dependent CMYK color space.
- [class var genericCMYK: NSColorSpace](nscolorspace/genericcmyk.md)
  A color space object that represents a device-independent CMYK color space.
- [class var deviceGray: NSColorSpace](nscolorspace/devicegray.md)
  A color space object that represents a calibrated or device-dependent gray color space.
- [class var genericGray: NSColorSpace](nscolorspace/genericgray.md)
  A color space object that represents a device-independent gray color space.
- [class var sRGB: NSColorSpace](nscolorspace/srgb.md)
  A color space object that represents an sRGB color space.
- [class var extendedSRGB: NSColorSpace](nscolorspace/extendedsrgb.md)
  A color space object that represents an extended sRGB color space.
- [class var displayP3: NSColorSpace](nscolorspace/displayp3.md)
  A color space object that represents a P3 Display color space.
- [class var genericGamma22Gray: NSColorSpace](nscolorspace/genericgamma22gray.md)
  A color space object that represents a gray color space with a gamma value of 2.2.
- [class var extendedGenericGamma22Gray: NSColorSpace](nscolorspace/extendedgenericgamma22gray.md)
  A color space object that represents an extended gray color space with a gamma value of 2.2.
- [class var adobeRGB1998: NSColorSpace](nscolorspace/adobergb1998.md)
  A color space object that represents an Adobe RGB (1998) color space.
### Getting the Color Spaces Available On the System
- [class func availableColorSpaces(with: NSColorSpace.Model) -> [NSColorSpace]](nscolorspace/availablecolorspaces(with:).md)
  Returns the list of color spaces available on the system that are displayed in the color panel, in the order they are displayed in the color panel.
### Initializing a Custom Color Space Object
- [init?(cgColorSpace: CGColorSpace)](nscolorspace/init(cgcolorspace:).md)
  Initializes and returns a color space object initialized from a Core Graphics color-space object.
- [init?(colorSyncProfile: UnsafeMutableRawPointer)](nscolorspace/init(colorsyncprofile:).md)
  Initializes and returns a color space object from the specified ColorSync profile.
- [init?(iccProfileData: Data)](nscolorspace/init(iccprofiledata:).md)
  Initializes and returns a color space object from the specified ICC profile.
### Accessing Color Space Data and Attributes
- [var cgColorSpace: CGColorSpace?](nscolorspace/cgcolorspace.md)
  The Core Graphics color-space object that represents a color space equivalent to the color space’s.
- [var colorSpaceModel: NSColorSpace.Model](nscolorspace/colorspacemodel.md)
  The model on which the color space is based.
- [NSColorSpace.Model](nscolorspace/model.md)
  Constants that describe the abstract model on which color space objects are based.
- [var colorSyncProfile: UnsafeMutableRawPointer?](nscolorspace/colorsyncprofile.md)
  The ColorSync profile from which the color space was created.
- [var iccProfileData: Data?](nscolorspace/iccprofiledata.md)
  The ICC profile data from which the color space was created.
- [var localizedName: String?](nscolorspace/localizedname.md)
  The localized name of the color space.
- [var numberOfColorComponents: Int](nscolorspace/numberofcolorcomponents.md)
  The number of components, excluding alpha, the color space supports.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSColor](nscolor.md)
  An object that stores color data and sometimes opacity (alpha value).
- [class NSColorList](nscolorlist.md)
  An ordered list of color objects, identified by keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspace)*