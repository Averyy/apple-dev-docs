# init(iccBasedNComponents:range:profile:alternate:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a device-independent color space that is defined according to the ICC color profile specification.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(iccBasedNComponents nComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)
```

```c
extern CGColorSpaceRefCGColorSpaceCreateICCBased(size_t nComponents, const CGFloat *range, CGDataProviderRef profile, CGColorSpaceRef alternate);
```

#### Return Value

A new ICC-based color space object, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](../cgcolorspacerelease.md).

#### Discussion

This function creates an ICC-based color space from an ICC color profile, as defined by the International Color Consortium. ICC profiles define the reproducible color gamut (the range of colors supported by a device) and other characteristics of a particular output device, providing a way to accurately transform the color space of one device to the color space of another. The ICC profile is usually provided by the manufacturer of the device. Additionally, some color monitors and printers contain electronically embedded ICC profile information, as do some bitmap formats such as TIFF. Colors in a device-independent color space should appear the same when displayed on different devices, to the extent that the capabilities of the device allow.

You may want to use this function for a color space that requires a detailed gamma, such as the piecewise transfer function used in sRGB or ITU-R BT.709, because this function can accurately represent these gamma curves.

## Parameters

- `nComponents`: The number of color components in the color space defined by the ICC profile data. This must match the number of components actually in the ICC profile and must equal 1, 3, or 4.
- `range`: An array of numbers that specify the minimum and maximum valid values of the corresponding color components. The size of the array is two times the number of components. If `c[k]` is the `k`the color component, the valid range is range`[2*k] ≤ c[k] ≤` range`[2*k+1]`.
- `profile`: A data provider that supplies the ICC profile.
- `alternate`: An alternate color space to use in case the ICC profile is not supported. The alternate color space must have `nComponents` color components. You must supply an alternate color space. If this parameter is `NULL`, then the function returns `NULL`.

## See Also

### Creating Color Spaces
- [init?(calibratedGrayWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: CGFloat)](./init%28calibratedgraywhitepoint,blackpoint,gamma%29.md)
  Creates a calibrated grayscale color space.
- [init?(calibratedRGBWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: UnsafePointer<CGFloat>?, matrix: UnsafePointer<CGFloat>?)](./init%28calibratedrgbwhitepoint,blackpoint,gamma,matrix%29.md)
  Creates a calibrated RGB color space.
- [init?(indexedBaseSpace: CGColorSpace, last: Int, colorTable: UnsafePointer<UInt8>)](./init%28indexedbasespace,last,colortable%29.md)
  Creates an indexed color space, consisting of colors specified by a color lookup table.
- [init?(labWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)](./init%28labwhitepoint,blackpoint,range%29.md)
  Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [init?(patternBaseSpace: CGColorSpace?)](./init%28patternbasespace%29.md)
  Creates a pattern color space.
- [init?(name: CFString)](./init%28name%29.md)
  Creates a specified type of Quartz color space.
- [init?(platformColorSpaceRef: UnsafeRawPointer)](./init%28platformcolorspaceref%29.md)
  Creates a platform-specific color space.
- [init?(iccData: CFTypeRef)](./init%28iccdata%29.md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
- [init?(propertyListPlist: CFPropertyList)](./init%28propertylistplist%29.md)
  Creates a color space from a property list.
- [func CGColorSpaceCreateDeviceRGB() -> CGColorSpace](../cgcolorspacecreatedevicergb%28%29.md)
  Creates a device-dependent RGB color space.
- [func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace](../cgcolorspacecreatedevicecmyk%28%29.md)
  Creates a device-dependent CMYK color space.
- [func CGColorSpaceCreateDeviceGray() -> CGColorSpace](../cgcolorspacecreatedevicegray%28%29.md)
  Creates a device-dependent grayscale color space.
- [init?(iccProfileData: CFData)](./init%28iccprofiledata%29.md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(iccbasedncomponents:range:profile:alternate:))*