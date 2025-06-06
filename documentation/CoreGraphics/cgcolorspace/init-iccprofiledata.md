# init(iccProfileData:)

**Framework**: Core Graphics  
**Kind**: init

Creates an ICC-based color space using the ICC profile contained in the specified data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(iccProfileData data: CFData)
```

#### Return Value

A new color space based on the specified profile.

## Parameters

- `data`: The data containing the ICC profile to set for the new color space.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(iccprofiledata:))*