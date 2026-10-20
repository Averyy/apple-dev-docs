# init(iccData:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates an ICC-based color space using the ICC profile contained in the specified data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init?(iccData data: CFTypeRef)
```

```c
extern CGColorSpaceRefCGColorSpaceCreateWithICCData(CFTypeRef data);
```

## Parameters

- `data`: The data containing the ICC profile to set for the new color space.

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
- [init?(labWhitePoint: UnsafePointer<CGFloat>, blackPoint: UnsafePointer<CGFloat>?, range: UnsafePointer<CGFloat>?)](./init%28labwhitepoint,blackpoint,range%29.md)
  Creates a device-independent color space that is relative to human color perception, according to the CIE L*a*b* standard.
- [init?(patternBaseSpace: CGColorSpace?)](./init%28patternbasespace%29.md)
  Creates a pattern color space.
- [init?(name: CFString)](./init%28name%29.md)
  Creates a specified type of Quartz color space.
- [init?(platformColorSpaceRef: UnsafeRawPointer)](./init%28platformcolorspaceref%29.md)
  Creates a platform-specific color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(iccdata:))*