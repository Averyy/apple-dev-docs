# init(platformColorSpaceRef:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a platform-specific color space.

**Availability**:
- iOS 9.0+ - Deprecated in 15.0
- iPadOS 9.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

> **Deprecated**: No longer supported

## Declaration

```swift
init?(platformColorSpaceRef ref: UnsafeRawPointer)
```

```c
extern CGColorSpaceRefCGColorSpaceCreateWithPlatformColorSpace(const void *ref);
```

## Return Value

A new color space, or `NULL` if unsuccessful. In Objective-C, you’re responsible for releasing this object by calling [`CGColorSpaceRelease`](../cgcolorspacerelease.md).

## Discussion

Colors in a device-dependent color space are not transformed or otherwise modified when displayed on an output device — that is, there is no attempt to maintain the visual appearance of a color. As a consequence, colors in a device color space often appear different when displayed on different output devices. For this reason, device color spaces are not recommended when color preservation is important.

## Parameters

- `ref`: A generic pointer to a platform-specific color space. In macOS, pass a `ColorSyncProfileRef`, which is a ColorSync profile. Quartz uses this pointer (and the underlying information) only during the function call.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorspace/init(platformcolorspaceref:))*