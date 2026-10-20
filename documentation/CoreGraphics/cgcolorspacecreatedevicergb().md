# CGColorSpaceCreateDeviceRGB()

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Creates a device-dependent RGB color space.

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
func CGColorSpaceCreateDeviceRGB() -> CGColorSpace
```

```c
extern CGColorSpaceRefCGColorSpaceCreateDeviceRGB();
```

#### Return Value

A device-dependent RGB color space. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](./cgcolorspacerelease.md). If unsuccessful, returns `NULL`.

#### Discussion

Colors in a device-dependent color space are not transformed or otherwise modified when displayed on an output device—that is, there is no attempt to maintain the visual appearance of a color. As a consequence, colors in a device color space often appear different when displayed on different output devices. For this reason, device color spaces are not recommended when color preservation is important.

## See Also

### Creating Color Spaces
- [init?(calibratedGrayWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: CGFloat)](./cgcolorspace/init%28calibratedgraywhitepoint,blackpoint,gamma%29.md)
  Creates a calibrated grayscale color space.
- [init?(calibratedRGBWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, gamma: UnsafePointer<CGFloat>?, matrix: UnsafePointer<CGFloat>?)](./cgcolorspace/init%28calibratedrgbwhitepoint,blackpoint,gamma,matrix%29.md)
  Creates a calibrated RGB color space.
- [init?(iccBasedNComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)](./cgcolorspace/init%28iccbasedncomponents,range,profile,alternate%29.md)
  Creates a device-independent color space that is defined according to the ICC color profile specification.
- [init?(indexedBaseSpace: CGColorSpace, last: Int, colorTable: UnsafePointer<UInt8>)](./cgcolorspace/init%28indexedbasespace,last,colortable%29.md)
  Creates an indexed color space, consisting of colors specified by a color lookup table.
- [init?(labWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)](./cgcolorspace/init%28labwhitepoint,blackpoint,range%29.md)
  Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [init?(patternBaseSpace: CGColorSpace?)](./cgcolorspace/init%28patternbasespace%29.md)
  Creates a pattern color space.
- [init?(name: CFString)](./cgcolorspace/init%28name%29.md)
  Creates a specified type of Quartz color space.
- [init?(platformColorSpaceRef: UnsafeRawPointer)](./cgcolorspace/init%28platformcolorspaceref%29.md)
  Creates a platform-specific color space.
- [init?(iccData: CFTypeRef)](./cgcolorspace/init%28iccdata%29.md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
- [init?(propertyListPlist: CFPropertyList)](./cgcolorspace/init%28propertylistplist%29.md)
  Creates a color space from a property list.
- [func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace](./cgcolorspacecreatedevicecmyk%28%29.md)
  Creates a device-dependent CMYK color space.
- [func CGColorSpaceCreateDeviceGray() -> CGColorSpace](./cgcolorspacecreatedevicegray%28%29.md)
  Creates a device-dependent grayscale color space.
- [init?(iccProfileData: CFData)](./cgcolorspace/init%28iccprofiledata%29.md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspacecreatedevicergb())*