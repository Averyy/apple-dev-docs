# NSColor

**Framework**: AppKit  
**Kind**: class

An object that stores color data and sometimes opacity (alpha value).

**Availability**:
- macOS ?+

## Declaration

```swift
class NSColor
```

#### Overview

Many methods in AppKit require you to specify color data using an [`NSColor`](nscolor.md) object; when drawing you use them to set the current fill and stroke colors. Color objects are immutable and thread-safe. You can create color objects in many ways:

- Load colors from an asset catalog. Colors created from assets can adapt automatically to system appearance changes.
- Use the semantic colors for custom UI elements, so that they match the appearance of other AppKit views; see [`UI Element Colors`](ui-element-colors.md).
- Use the adaptable system colors, such as [`systemBlue`](nscolor/systemblue.md), when you want a specific tint that looks correct in both light and dark environments.
- Create a color object from another object, such as a Core Graphics representation of a color, or a Core Image color.
- Create a color from an [`NSImage`](nsimage.md) object, and paint a repeating pattern instead of using a solid color.
- Create a color by applying a transform to another [`NSColor`](nscolor.md) object. For example, you might perform a blend operation between two colors, or you might create a color that represents the same color, but in a different color space.
- Create custom colors using raw component values, and a variety of color spaces, when you need to represent user-specified colors.

For user-specified colors, you can also display a color panel and let the user specify the color. For information about color panels, see [`NSColorPanel`](nscolorpanel.md).

##### Color and Color Spaces

A color object is typically represented internally as a Core Graphics color ([`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor)) in a Core Graphics color space ([`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace)). Colors can also be created in extended color spaces:

- [`extendedSRGB`](nscolorspace/extendedsrgb.md)
- [`extendedGenericGamma22Gray`](nscolorspace/extendedgenericgamma22gray.md)

When you need to worry about color spaces, use extended color spaces as working color spaces. When you need to worry about representing that color as closely as possible in a specific color space, convert the color from the extended color space into the target color space.

When working in an extended color space, color values are not clamped to fit inside the color gamut, meaning that component values may be less than `0.0` or greater than `1.0`. When displayed on an sRGB display, such colors are outside the gamut and won’t render accurately. However, extended color spaces are useful as working color spaces when you want a pixel format and representation that other color spaces can be easily converted into. For example, a color in the Display P3 color space can convert to an extended sRGB format, even if it isn’t within the sRGB color gamut. While some of the converted color’s values are outside of the 0-1.0 range, the color renders correctly when viewed on a device with a P3 display gamut.

It is a programmer error to access color components of a color space that the `NSColor` object does not support. For example, you cannot access the [`redComponent`](nscolor/redcomponent.md) property and [`getRed(_:green:blue:alpha:)`](nscolor/getred(_:green:blue:alpha:).md) method on a color that uses the CMYK color space. Further, the [`getComponents(_:)`](nscolor/getcomponents(_:).md) method and [`numberOfComponents`](nscolor/numberofcomponents.md) property work only in color spaces that have individual components. As such, they return the components of color objects as individual floating-point values regardless of whether they’re based on [`NSColorSpace`](nscolorspace.md) objects or named color spaces. However, older component-fetching methods such as [`getRed(_:green:blue:alpha:)`](nscolor/getred(_:green:blue:alpha:).md) are effective only on color objects based on named color spaces.

If you have a color object in an unknown color space and you want to extract its components, convert the color object to a known color space and then use the component accessor methods of that color space.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/visual-design/color/).

## Topics

### Getting and Creating Colors
- [UI Element Colors](ui-element-colors.md)
  Retrieve standard color objects for use with windows, controls, labels, text, selections and other content in your app.
- [Standard Colors](standard-colors.md)
  Retrieve the standard color objects for common colors like red, blue, green, black, white, and more.
- [Color Creation](color-creation.md)
  Load colors from asset catalogs, and create colors from raw component values, such as those used by grayscale, RGB, HSB, and CMYK colors.
### Applying Specific Appearances to Colors
- [func withSystemEffect(NSColor.SystemEffect) -> NSColor](nscolor/withsystemeffect(_:).md)
  Returns a new color object that represents the current color modified to include the specified visual effect.
- [NSColor.SystemEffect](nscolor/systemeffect.md)
  Constants for user interactions that change the appearance of a view or control.
### Transforming Existing Color Objects
- [func usingColorSpace(NSColorSpace) -> NSColor?](nscolor/usingcolorspace(_:).md)
  Creates a new color object representing the color of the current color object in the specified color space.
- [func blended(withFraction: CGFloat, of: NSColor) -> NSColor?](nscolor/blended(withfraction:of:).md)
  Creates a new color object whose component values are a weighted sum of the current color object and the specified color object’s.
- [func withAlphaComponent(CGFloat) -> NSColor](nscolor/withalphacomponent(_:).md)
  Creates a new color object that has the same color space and component values as the current color object, but the specified alpha component.
- [func highlight(withLevel: CGFloat) -> NSColor?](nscolor/highlight(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the highlight color.
- [func shadow(withLevel: CGFloat) -> NSColor?](nscolor/shadow(withlevel:).md)
  Creates a new color object that represents a blend between the current color and the shadow color.
- [func usingColorSpaceName(NSColorSpaceName) -> NSColor?](nscolor/usingcolorspacename(_:).md)
  Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space.
- [func usingColorSpaceName(NSColorSpaceName?, device: [NSDeviceDescriptionKey : Any]?) -> NSColor?](nscolor/usingcolorspacename(_:device:).md)
  Creates a new color object for the same color, but in the specified color space and specific to the provided device.
### Determining the Alpha Support of Colors
- [class var ignoresAlpha: Bool](nscolor/ignoresalpha.md)
  A Boolean value that indicates whether the app supports alpha.
### Copying and Pasting Color Information
- [init?(from: NSPasteboard)](nscolor/init(from:).md)
  Creates a color object from color data currently on the pasteboard.
- [func write(to: NSPasteboard)](nscolor/write(to:).md)
  Writes the color object’s data to the specified pasteboard.
### Retrieving Component Values from Color Objects
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getcyan(_:magenta:yellow:black:alpha:).md)
  Returns the color object’s CMYK and opacity values.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/gethue(_:saturation:brightness:alpha:).md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getwhite(_:alpha:).md)
  Returns the grayscale and alpha values of the color.
- [var numberOfComponents: Int](nscolor/numberofcomponents.md)
  The number of components in the color.
- [func getComponents(UnsafeMutablePointer<CGFloat>)](nscolor/getcomponents(_:).md)
  Returns the components of the color as an array.
### Retrieving Individual Components
- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var whiteComponent: CGFloat](nscolor/whitecomponent.md)
  The white component value of the color.
- [var redComponent: CGFloat](nscolor/redcomponent.md)
  The red component value of the color.
- [var greenComponent: CGFloat](nscolor/greencomponent.md)
  The green component value of the color.
- [var blueComponent: CGFloat](nscolor/bluecomponent.md)
  The blue component value of the color.
- [var cyanComponent: CGFloat](nscolor/cyancomponent.md)
  The cyan component value of the color.
- [var magentaComponent: CGFloat](nscolor/magentacomponent.md)
  The magenta component value of the color.
- [var yellowComponent: CGFloat](nscolor/yellowcomponent.md)
  The yellow component value of the color.
- [var blackComponent: CGFloat](nscolor/blackcomponent.md)
  The black component value of the color.
- [var hueComponent: CGFloat](nscolor/huecomponent.md)
  The hue component value of the color.
- [var saturationComponent: CGFloat](nscolor/saturationcomponent.md)
  The saturation component value of the color.
- [var brightnessComponent: CGFloat](nscolor/brightnesscomponent.md)
  The brightness component value of the color.
- [var catalogNameComponent: NSColorList.Name](nscolor/catalognamecomponent.md)
  The catalog containing the color’s name.
- [var localizedCatalogNameComponent: String](nscolor/localizedcatalognamecomponent.md)
  The localized version of the catalog name containing the color.
- [var colorNameComponent: NSColor.Name](nscolor/colornamecomponent.md)
  The name of the color.
- [var localizedColorNameComponent: String](nscolor/localizedcolornamecomponent.md)
  The localized version of the color name.
### Working with the Color Space
- [var type: NSColor.ColorType](nscolor/type.md)
  The type of the color object.
- [func usingType(NSColor.ColorType) -> NSColor?](nscolor/usingtype(_:).md)
  Returns a version of the color object that is compatible with the specified color type.
- [NSColor.ColorType](nscolor/colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpace: NSColorSpace](nscolor/colorspace.md)
  The color space associated with the color.
- [var colorSpaceName: NSColorSpaceName](nscolor/colorspacename.md)
  The name of the color space associated with the color.
- [struct NSColorSpaceName](nscolorspacename.md)
  Constants that specify color space names.
### Retrieving Core Graphics Color Information
- [var cgColor: CGColor](nscolor/cgcolor.md)
  The Core Graphics color object corresponding to the color.
### Drawing with Colors
- [func drawSwatch(in: NSRect)](nscolor/drawswatch(in:).md)
  Draws the current color in the specified rectangle.
- [func set()](nscolor/set.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [func setFill()](nscolor/setfill.md)
  Sets the fill color of subsequent drawing to the color object’s color.
- [func setStroke()](nscolor/setstroke.md)
  Sets the stroke color of subsequent drawing to the color object’s color.
### Determining When Colors Change
- [class let systemColorsDidChangeNotification: NSNotification.Name](nscolor/systemcolorsdidchangenotification.md)
  Sent when the system colors have changed, such as through a system control panel interface.
- [class let currentControlTintDidChangeNotification: NSNotification.Name](nscolor/currentcontroltintdidchangenotification.md)
  Sent after the user changes control tint preference.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityColor](nsaccessibilitycolor.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](nspasteboardreading.md)
- [NSPasteboardWriting](nspasteboardwriting.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [class NSColorList](nscolorlist.md)
  An ordered list of color objects, identified by keys.
- [class NSColorSpace](nscolorspace.md)
  An object that represents a custom color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor)*