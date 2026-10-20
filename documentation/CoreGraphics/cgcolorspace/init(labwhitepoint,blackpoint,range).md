# init(labWhitePoint:blackPoint:range:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.

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
init?(labWhitePoint whitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)
```

```c
extern CGColorSpaceRefCGColorSpaceCreateLab(const CGFloat whitePoint[3], const CGFloat blackPoint[3], const CGFloat range[4]);
```

#### Return Value

A new L*a*b* color space, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](../cgcolorspacerelease.md).

#### Discussion

The CIE L*a*b* space is a nonlinear transformation of the Munsell color notation system (a system which specifies colors by hue, value, and saturation—or “chroma”—values), designed to match perceived color difference with quantitative distance in color space. The L* component represents the lightness value, the a* component represents values running from green to red, and the b* component represents values running from blue to yellow. This roughly corresponds to the way the human brain is thought to decode colors. Colors in a device-independent color space should appear the same when displayed on different devices, to the extent that the capabilities of the device allow.

## Parameters

- `whitePoint`: An array of 3 numbers that specify the tristimulus value, in the CIE 1931 XYZ-space, of the diffuse white point.
- `blackPoint`: An array of 3 numbers that specify the tristimulus value, in CIE 1931 XYZ-space, of the diffuse black point.
- `range`: An array of 4 numbers that specify the range of valid values for the a* and b* components of the color space. The a* component represents values running from green to red, and the b* component represents values running from blue to yellow.

## See Also

### Creating Color Spaces
- [init?(calibratedGrayWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: CGFloat)](./init%28calibratedgraywhitepoint,blackpoint,gamma%29.md)
  Creates a calibrated grayscale color space.
- [init?(calibratedRGBWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: UnsafePointer<CGFloat>?, matrix: UnsafePointer<CGFloat>?)](./init%28calibratedrgbwhitepoint,blackpoint,gamma,matrix%29.md)
  Creates a calibrated RGB color space.
- [init?(iccBasedNComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)](./init%28iccbasedncomponents,range,profile,alternate%29.md)
  Creates a device-independent color space that is defined according to the ICC color profile specification.
- [init?(indexedBaseSpace: CGColorSpace, last: Int, colorTable: UnsafePointer<UInt8>)](./init%28indexedbasespace,last,colortable%29.md)
  Creates an indexed color space, consisting of colors specified by a color lookup table.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(labwhitepoint:blackpoint:range:))*