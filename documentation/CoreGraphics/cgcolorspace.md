# CGColorSpace

**Framework**: Core Graphics  
**Kind**: class

A profile that specifies how to interpret a color value for display.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGColorSpace
```

#### Overview

A color space is multi-dimensional, and each dimension represents a specific color component. For example, the colors in an RGB color space have three dimensions or components—red, green, and blue. The intensity of each component is represented by floating point values—their range and meaning depends on the color space in question.

Different types of devices (scanners, monitors, printers) operate within different color spaces (RGB, CMYK, grayscale). Additionally, two devices of the same type (for example, color displays from different manufacturers) may operate within the same kind of color space, yet still produce a different range of colors, or gamut. Color spaces that are correctly specified ensure that an image has a consistent appearance regardless of the output device.

Core Graphics supports several kinds of color spaces:

- Calibrated color spaces ensure that colors appear the same when displayed on different devices. The visual appearance of the color is preserved, as far as the capabilities of the device allow.
- Device-dependent color spaces are tied to the system of color representation of a particular device. Device color spaces are not recommended when high-fidelity color preservation is important.
- Special color spaces—indexed and pattern. An indexed color space contains a color table with up to 256 entries and a base color space to which the color table entries are mapped. Each entry in the color table specifies one color in the base color space. A pattern color space is used when stroking or filling with a pattern.

## Topics

### Creating Color Spaces
- [init?(calibratedGrayWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: CGFloat)](cgcolorspace/init(calibratedgraywhitepoint:blackpoint:gamma:).md)
  Creates a calibrated grayscale color space.
- [init?(calibratedRGBWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: UnsafePointer<CGFloat>?, matrix: UnsafePointer<CGFloat>?)](cgcolorspace/init(calibratedrgbwhitepoint:blackpoint:gamma:matrix:).md)
  Creates a calibrated RGB color space.
- [init?(iccBasedNComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)](cgcolorspace/init(iccbasedncomponents:range:profile:alternate:).md)
  Creates a device-independent color space that is defined according to the ICC color profile specification.
- [init?(indexedBaseSpace: CGColorSpace, last: Int, colorTable: UnsafePointer<UInt8>)](cgcolorspace/init(indexedbasespace:last:colortable:).md)
  Creates an indexed color space, consisting of colors specified by a color lookup table.
- [init?(labWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)](cgcolorspace/init(labwhitepoint:blackpoint:range:).md)
  Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [init?(patternBaseSpace: CGColorSpace?)](cgcolorspace/init(patternbasespace:).md)
  Creates a pattern color space.
- [init?(name: CFString)](cgcolorspace/init(name:).md)
  Creates a specified type of Quartz color space.
- [init?(platformColorSpaceRef: UnsafeRawPointer)](cgcolorspace/init(platformcolorspaceref:).md)
  Creates a platform-specific color space.
- [init?(iccData: CFTypeRef)](cgcolorspace/init(iccdata:).md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
- [init?(propertyListPlist: CFPropertyList)](cgcolorspace/init(propertylistplist:).md)
  Creates a color space from a property list.
- [func CGColorSpaceCreateDeviceRGB() -> CGColorSpace](cgcolorspacecreatedevicergb().md)
  Creates a device-dependent RGB color space.
- [func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace](cgcolorspacecreatedevicecmyk().md)
  Creates a device-dependent CMYK color space.
- [func CGColorSpaceCreateDeviceGray() -> CGColorSpace](cgcolorspacecreatedevicegray().md)
  Creates a device-dependent grayscale color space.
- [init?(iccProfileData: CFData)](cgcolorspace/init(iccprofiledata:).md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
### Examining a Color Space
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
- [func copyPropertyList() -> CFPropertyList?](cgcolorspace/copypropertylist.md)
  Returns a copy of the color space’s properties.
- [var iccData: CFData?](cgcolorspace/iccdata.md)
  Returns a copy of the ICC profile of the provided color space.
- [var name: CFString?](cgcolorspace/name.md)
  Returns the name used to create the specified color space.
- [var supportsOutput: Bool](cgcolorspace/supportsoutput.md)
  Returns a Boolean indicating whether the color space can be used as a destination color space.
- [var isWideGamutRGB: Bool](cgcolorspace/iswidegamutrgb.md)
  Returns whether the RGB color space covers a significant portion of the NTSC color gamut.
### Accessing System-Defined Color Spaces
- [class let displayP3: CFString](cgcolorspace/displayp3.md)
  The Display P3 color space, created by Apple.
- [class let displayP3_HLG: CFString](cgcolorspace/displayp3_hlg.md)
  The Display P3 color space, using the HLG transfer function.
- [class let displayP3_PQ_EOTF: CFString](cgcolorspace/displayp3_pq_eotf.md)
  The Display P3 color space, using the PQ transfer function.
- [class let extendedLinearDisplayP3: CFString](cgcolorspace/extendedlineardisplayp3.md)
  The Display P3 color space with a linear transfer function and extended-range values.
- [class let sRGB: CFString](cgcolorspace/srgb.md)
  The standard Red Green Blue (sRGB) color space.
- [class let linearSRGB: CFString](cgcolorspace/linearsrgb.md)
  The sRGB color space with a linear transfer function.
- [class let extendedSRGB: CFString](cgcolorspace/extendedsrgb.md)
  The extended sRGB color space.
- [class let extendedLinearSRGB: CFString](cgcolorspace/extendedlinearsrgb.md)
  The sRGB color space with a linear transfer function and extended-range values.
- [class let genericGrayGamma2_2: CFString](cgcolorspace/genericgraygamma2_2.md)
  The generic gray color space that has an exponential transfer function with a power of 2.2.
- [class let extendedGray: CFString](cgcolorspace/extendedgray.md)
  The extended gray color space.
- [class let linearGray: CFString](cgcolorspace/lineargray.md)
  The gray color space using a linear transfer function.
- [class let extendedLinearGray: CFString](cgcolorspace/extendedlineargray.md)
  The extended gray color space with a linear transfer function.
- [class let genericCMYK: CFString](cgcolorspace/genericcmyk.md)
  The generic CMYK color space.
- [class let genericRGBLinear: CFString](cgcolorspace/genericrgblinear.md)
  The generic RGB color space with a linear transfer function.
- [class let genericXYZ: CFString](cgcolorspace/genericxyz.md)
  The XYZ color space, as defined by the CIE 1931 standard.
- [class let genericLab: CFString](cgcolorspace/genericlab.md)
  The generic LAB color space.
- [class let acescgLinear: CFString](cgcolorspace/acescglinear.md)
  The ACEScg color space.
- [class let adobeRGB1998: CFString](cgcolorspace/adobergb1998.md)
  The Adobe RGB (1998) color space.
- [class let dcip3: CFString](cgcolorspace/dcip3.md)
  The DCI P3 color space, which is the digital cinema standard.
- [class let itur_709: CFString](cgcolorspace/itur_709.md)
  The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.709 color space.
- [class let rommrgb: CFString](cgcolorspace/rommrgb.md)
  The Reference Output Medium Metric (ROMM) RGB color space.
- [class let itur_2020: CFString](cgcolorspace/itur_2020.md)
  The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space.
- [class let itur_2020_HLG: CFString](cgcolorspace/itur_2020_hlg.md)
  The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the HLG transfer function.
- [class let itur_2020_PQ_EOTF: CFString](cgcolorspace/itur_2020_pq_eotf.md)
  The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with the PQ transfer function.
- [class let extendedLinearITUR_2020: CFString](cgcolorspace/extendedlinearitur_2020.md)
  The recommendation of the International Telecommunication Union (ITU) Radiocommunication sector for the BT.2020 color space, with a linear transfer function and extended range values.
- [class let coreMedia709: CFString](cgcolorspace/coremedia709.md)
- [class let displayP3_PQ: CFString](cgcolorspace/displayp3_pq.md)
- [class let extendedDisplayP3: CFString](cgcolorspace/extendeddisplayp3.md)
- [class let extendedITUR_2020: CFString](cgcolorspace/extendeditur_2020.md)
- [class let itur_2020_PQ: CFString](cgcolorspace/itur_2020_pq.md)
- [class let itur_2020_sRGBGamma: CFString](cgcolorspace/itur_2020_srgbgamma.md)
- [class let itur_2100_HLG: CFString](cgcolorspace/itur_2100_hlg.md)
- [class let itur_2100_PQ: CFString](cgcolorspace/itur_2100_pq.md)
- [class let itur_709_HLG: CFString](cgcolorspace/itur_709_hlg.md)
- [class let itur_709_PQ: CFString](cgcolorspace/itur_709_pq.md)
- [class let linearDisplayP3: CFString](cgcolorspace/lineardisplayp3.md)
- [class let linearITUR_2020: CFString](cgcolorspace/linearitur_2020.md)
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgcolorspace/typeid.md)
  Returns the Core Foundation type identifier for Quartz color spaces.
### Data Types
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
### Instance Methods
- [func isHDR() -> Bool](cgcolorspace/ishdr.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGColor](cgcolor.md)
  A set of components that define a color, with a color space specifying how to interpret them.
- [class CGColorConversionInfo](cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [class CGFont](cgfont.md)
  A set of character glyphs and layout information for drawing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace)*