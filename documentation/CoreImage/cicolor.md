# CIColor

**Framework**: Core Image  
**Kind**: class

The Core Image class that defines a color object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIColor
```

## Mentions

- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)

#### Overview

Use `CIColor` instances in conjunction with other Core Image classes, such as [`CIFilter`](cifilter-swift.class.md) and [`CIKernel`](cikernel.md). Many of the built-in Core Image filters have one or more `CIColor` inputs that you can set to affect the filter’s behavior.

##### Color Model

A color is defined as a N-dimensional model where each dimension’s color component is represented by intensity values. A color component may also be referred to as a color channel. An RGB color model, for example, is three-dimensional and the red, green, and blue component intensities define each unique color.

##### Color Space

A color is also defined by a color space that locates the axes of N-dimensional model within the greater volume of human perceivable colors.  Core Image uses `CGColorSpace` instances to specify a variety of different color spaces such as sRGB, P3, BT.2020, etc. The `CGColorSpace` also defines if the color space is coded linearly or in a non-linear perceptual curve. (For more information on `CGColorSpace` see [`CGColorSpace`](https://developer.apple.com/documentation/coregraphics/cgcolorspace))

##### Color Range

Standard dynamic range (SDR) color color component values range from `0.0` to `1.0`, with `0.0` representing an 0% of that component and `1.0` representing 100%. In contrast, high dynamic range (HDR) color values can be less than `0.0` (for more saturation) or greater than `1.0` (for more brightness).

##### Color Opacity

`CIColor` instances also have an alpha component, which represents the opacity of the color, with 0.0 meaning completely transparent and 1.0 meaning completely opaque. If a color does not have an explicit alpha component, Core Image assumes that the alpha component equals 1.0. With `CIColor` that color components values are not premultiplied. So for example, a semi-transparent pure red `CIColor` is represented by RGB `1.0,0.0,0.0` and A `0.5`.  In contrast color components values in [`CIImage`](ciimage.md) buffers or read in [`CIKernel`](cikernel.md) samplers are premultiplied by default.

## Topics

### Initializing Color Objects
- [init(cgColor: CGColor)](cicolor/init(cgcolor:)-1hzk4.md)
  Create a Core Image color object with a Core Graphics color object.
- [convenience init(color: UIColor)](cicolor/init(color:).md)
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cicolor/init(red:green:blue:alpha:).md)
  Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.
### Creating Color Objects
- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](cicolor/init(red:green:blue:).md)
  Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [convenience init(string: String)](cicolor/init(string:).md)
  Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:)-2og6y.md)
  Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:)-5mvff.md)
  Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.
### Getting Color Components
- [var colorSpace: CGColorSpace](cicolor/colorspace.md)
  Returns the `CGColorSpace` associated with the color
- [var components: UnsafePointer<CGFloat>](cicolor/components.md)
  Return a pointer to an array of `CGFloat` values including alpha.
- [var numberOfComponents: Int](cicolor/numberofcomponents.md)
  Returns the color components of the color including alpha.
- [var red: CGFloat](cicolor/red-swift.property.md)
  Returns the unpremultiplied red component of the color.
- [var green: CGFloat](cicolor/green-swift.property.md)
  Returns the unpremultiplied green component of the color.
- [var blue: CGFloat](cicolor/blue-swift.property.md)
  Returns the unpremultiplied blue component of the color.
- [var alpha: CGFloat](cicolor/alpha.md)
  Returns the alpha value of the color.
- [var stringRepresentation: String](cicolor/stringrepresentation.md)
  Returns a formatted string with the unpremultiplied color and alpha components of the color.
### Creating a CIColor Object with Preset Components
- [class var black: CIColor](cicolor/black.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,0` and alpha value `1`.
- [class var blue: CIColor](cicolor/blue-swift.type.property.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,1` and alpha value `1`.
- [class var clear: CIColor](cicolor/clear.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,0` and alpha value `0`.
- [class var cyan: CIColor](cicolor/cyan.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,1,1` and alpha value `1`.
- [class var gray: CIColor](cicolor/gray.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0.5,0.5,0.5` and alpha value `1`.
- [class var green: CIColor](cicolor/green-swift.type.property.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,1,0` and alpha value `1`.
- [class var magenta: CIColor](cicolor/magenta.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,0,1` and alpha value `1`.
- [class var red: CIColor](cicolor/red-swift.type.property.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,0,0` and alpha value `1`.
- [class var white: CIColor](cicolor/white.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,1,1` and alpha value `1`.
- [class var yellow: CIColor](cicolor/yellow.md)
  Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,1,0` and alpha value `1`.
### Initializers
- [convenience init(CGColor: CGColor)](cicolor/init(cgcolor:)-2n26w.md)
- [init(CGColor: CGColor)](cicolor/init(cgcolor:)-2nx98.md)
- [init?(coder: NSCoder)](cicolor/init(coder:).md)
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:alpha:colorspace:)-8yg0z.md)
  Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [convenience init?(red: CGFloat, green: CGFloat, blue: CGFloat, colorSpace: CGColorSpace)](cicolor/init(red:green:blue:colorspace:)-6d8o.md)
  Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CIFilter](cifilter-swift.class.md)
  An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIVector](civector.md)
  The Core Image class that defines a vector object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor)*