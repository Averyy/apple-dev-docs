# init(indexedBaseSpace:last:colorTable:)

**Framework**: Core Graphics  
**Kind**: init

Creates an indexed color space, consisting of colors specified by a color lookup table.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(indexedBaseSpace baseSpace: CGColorSpace, last lastIndex: Int, colorTable: UnsafePointer<UInt8>)
```

#### Return Value

A new indexed color space object, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](cgcolorspacerelease.md).

#### Discussion

An indexed color space contains a color table with up to 255 entries, and a base color space to which the color table entries are mapped. Each entry in the color table specifies one color in the base color space. A value in an indexed color space is treated as an index into the color table of the color space. The data in the table is in meshed format. (For example, for an RGB color space the values are R, G, B, R, G, B, and so on.)

## Parameters

- `baseSpace`: The color space on which the color table is based.
- `lastIndex`: The maximum valid index value for the color table. The value must be less than or equal to 255.
- `colorTable`: An array of   bytes, where   is the number of color components in the base color space. Each byte is an unsigned integer in the range   to   that is scaled to the range of the corresponding color component in the base color space.

## See Also

- [init?(calibratedGrayWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: CGFloat)](cgcolorspace/init(calibratedgraywhitepoint:blackpoint:gamma:).md)
  Creates a calibrated grayscale color space.
- [init?(calibratedRGBWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: UnsafePointer<CGFloat>?, matrix: UnsafePointer<CGFloat>?)](cgcolorspace/init(calibratedrgbwhitepoint:blackpoint:gamma:matrix:).md)
  Creates a calibrated RGB color space.
- [init?(iccBasedNComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)](cgcolorspace/init(iccbasedncomponents:range:profile:alternate:).md)
  Creates a device-independent color space that is defined according to the ICC color profile specification.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(indexedbasespace:last:colortable:))*