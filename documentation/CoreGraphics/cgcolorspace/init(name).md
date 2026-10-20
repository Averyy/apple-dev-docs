# init(name:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a specified type of Quartz color space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(name: CFString)
```

```c
extern CGColorSpaceRefCGColorSpaceCreateWithName(CFStringRef name);
```

#### Return Value

A new generic color space, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](../cgcolorspacerelease.md).

#### Discussion

You can use this function to create a generic color space. For more information, see [Accessing System-Defined Color Spaces](../cgcolorspace.md#Accessing-System-Defined-Color-Spaces).

## Parameters

- `name`: A color space name. See [Accessing System-Defined Color Spaces](../cgcolorspace.md#Accessing-System-Defined-Color-Spaces) for a list of the valid Quartz-defined names.

## See Also

### Related Documentation
- [var name: CFString?](./name.md)
  Returns the name used to create the specified color space.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(name:))*