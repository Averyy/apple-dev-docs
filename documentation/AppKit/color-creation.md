# Color Creation

**Framework**: AppKit

Load colors from asset catalogs, and create colors from raw component values, such as those used by grayscale, RGB, HSB, and CMYK colors.

## Topics

### Loading Color Objects from Asset Catalogs
- [init?(named: NSColor.Name)](nscolor/init(named:).md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.
- [init?(named: NSColor.Name, bundle: Bundle?)](nscolor/init(named:bundle:).md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](nscolor/init(catalogname:colorname:).md)
  Creates a color object using the specified asset catalog and color names.
- [typealias Name](nscolor/name.md)
  The name of a color.
### Creating a Color Using RGB Components
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(srgbred:green:blue:alpha:).md)
  Creates a color object from the specified components in the sRGB colorspace.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(displayp3red:green:blue:alpha:).md)
  Creates a color object from the specified components in the Display P3 color space.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(red:green:blue:alpha:).md)
  Creates a color object with the specified red, green, blue, and alpha channel values.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(calibratedred:green:blue:alpha:).md)
  Creates a color object using the given opacity and RGB components.
- [init(deviceRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](nscolor/init(devicered:green:blue:alpha:).md)
  Creates a color object using the given opacity value and RGB components.
### Creating a Color Using HSB Components
- [init(calibratedHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(calibratedhue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity and HSB color space components.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(devicehue:saturation:brightness:alpha:).md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(hue:saturation:brightness:alpha:).md)
  Creates a color object with the specified hue, saturation, brightness, and alpha channel values.
- [init(colorSpace: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](nscolor/init(colorspace:hue:saturation:brightness:alpha:).md)
  Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.
### Creating a Color Using CMYK Components
- [init(deviceCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](nscolor/init(devicecyan:magenta:yellow:black:alpha:).md)
  Creates a color object using the given opacity value and CMYK components.
### Creating a Color Using White Components
- [init(white: CGFloat, alpha: CGFloat)](nscolor/init(white:alpha:).md)
  Creates a color object with the specified brightness and alpha channel values.
- [init(calibratedWhite: CGFloat, alpha: CGFloat)](nscolor/init(calibratedwhite:alpha:).md)
  Creates a color object using the given opacity and grayscale values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](nscolor/init(devicewhite:alpha:).md)
  Creates a color object using the given opacity and grayscale values.
- [init(genericGamma22White: CGFloat, alpha: CGFloat)](nscolor/init(genericgamma22white:alpha:).md)
  Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.
### Creating a Pattern-Based Color
- [init(patternImage: NSImage)](nscolor/init(patternimage:).md)
  Creates a color object that uses the specified image pattern to paint the target area.
- [var patternImage: NSImage](nscolor/patternimage.md)
  The pattern image used to paint the target area.
### Creating a Color Dynamically
- [init(name: NSColor.Name?, dynamicProvider: (NSAppearance) -> NSColor)](nscolor/init(name:dynamicprovider:).md)
  Creates a dynamic catalog color with a provider that’s used to resolve the exact color value, calculated on first use.
### Creating a Color in an Arbitrary Color Space
- [init(colorSpace: NSColorSpace, components: UnsafePointer<CGFloat>, count: Int)](nscolor/init(colorspace:components:count:).md)
  Creates a color object from the specified components of the given color space.
### Creating a System Tint Color
- [init(for: NSControlTint)](nscolor/init(for:).md)
  Returns the color object specified by the given control tint.
- [enum NSControlTint](nscontroltint.md)
  Constants for specifying a cell’s tint color.
### Converting Other Types of Color Objects
- [convenience init(Color)](nscolor/init(_:).md)
- [init?(cgColor: CGColor)](nscolor/init(cgcolor:).md)
  Creates a color object using the specified Core Graphics color.
- [init(CIColor: CIColor)](nscolor/init(cicolor:).md)
  Creates a color object from the specified Core Image color.
### Creating Color Objects
- [init()](nscolor/init.md)
  Initializes the color object.
- [init?(coder: NSCoder)](nscolor/init(coder:).md)
  Creates a color object from data in an unarchiver.
- [convenience init(resource: ColorResource)](nscolor/init(resource:).md)

## See Also

- [UI Element Colors](ui-element-colors.md)
  Retrieve standard color objects for use with windows, controls, labels, text, selections and other content in your app.
- [Standard Colors](standard-colors.md)
  Retrieve the standard color objects for common colors like red, blue, green, black, white, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/color-creation)*