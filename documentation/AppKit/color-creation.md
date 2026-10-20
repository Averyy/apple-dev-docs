# Color creation

**Framework**: AppKit  
**Role**: API Collection

Load colors from asset catalogs, and create colors from raw component values, such as those used by grayscale, RGB, HSB, and CMYK colors.

## Topics

### Loading color objects from asset catalogs
- [init?(named: NSColor.Name)](./nscolor/init%28named%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the app’s main bundle.
- [init?(named: NSColor.Name, bundle: Bundle?)](./nscolor/init%28named,bundle%29.md)
  Creates a color object from the provided name, which corresponds to a color in the default asset catalog of the specified bundle.
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](./nscolor/init%28catalogname,colorname%29.md)
  Creates a color object using the specified asset catalog and color names.
- [typealias Name](./nscolor/name.md)
  The name of a color.
### Creating a color using RGB components
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./nscolor/init%28srgbred,green,blue,alpha%29-9oz51.md)
  Creates a color object from the specified components in the sRGB colorspace.
- [init(displayP3Red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./nscolor/init%28displayp3red,green,blue,alpha%29.md)
  Creates a color object from the specified components in the Display P3 color space.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./nscolor/init%28red,green,blue,alpha%29.md)
  Creates a color object with the specified red, green, blue, and alpha channel values.
- [init(calibratedRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./nscolor/init%28calibratedred,green,blue,alpha%29.md)
  Creates a color object using the given opacity and RGB components.
- [init(deviceRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](./nscolor/init%28devicered,green,blue,alpha%29.md)
  Creates a color object using the given opacity value and RGB components.
### Creating a color using HSB components
- [init(calibratedHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./nscolor/init%28calibratedhue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity and HSB color space components.
- [init(deviceHue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./nscolor/init%28devicehue,saturation,brightness,alpha%29.md)
  Creates a color object using the given opacity value and HSB color space components.
- [init(hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./nscolor/init%28hue,saturation,brightness,alpha%29.md)
  Creates a color object with the specified hue, saturation, brightness, and alpha channel values.
- [init(colorSpace: NSColorSpace, hue: CGFloat, saturation: CGFloat, brightness: CGFloat, alpha: CGFloat)](./nscolor/init%28colorspace,hue,saturation,brightness,alpha%29.md)
  Creates a color object with the specified color space, hue, saturation, brightness, and alpha channel values.
### Creating a color using CMYK components
- [init(deviceCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](./nscolor/init%28devicecyan,magenta,yellow,black,alpha%29.md)
  Creates a color object using the given opacity value and CMYK components.
### Creating a color using white components
- [init(white: CGFloat, alpha: CGFloat)](./nscolor/init%28white,alpha%29.md)
  Creates a color object with the specified brightness and alpha channel values.
- [init(calibratedWhite: CGFloat, alpha: CGFloat)](./nscolor/init%28calibratedwhite,alpha%29.md)
  Creates a color object using the given opacity and grayscale values.
- [init(deviceWhite: CGFloat, alpha: CGFloat)](./nscolor/init%28devicewhite,alpha%29.md)
  Creates a color object using the given opacity and grayscale values.
- [init(genericGamma22White: CGFloat, alpha: CGFloat)](./nscolor/init%28genericgamma22white,alpha%29.md)
  Returns a color object with the specified white and alpha values in the GenericGamma22 colorspace.
### Creating a high dynamic range (HDR) color
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, linearExposure: CGFloat)](./nscolor/init%28red,green,blue,alpha,linearexposure%29.md)
  Generates an HDR color in the extended sRGB colorspace by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `linearExposure` is a value >= 1. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `linearExposure `. The produced color will have a `contentHeadroom` equal to `linearExposure`. Each doubling of `linearExposure` produces a color that is twice as bright.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat, exposure: CGFloat)](./nscolor/init%28red,green,blue,alpha,exposure%29.md)
  Generates an HDR color in the extended sRGB colorspace by applying an exposure to the SDR color defined by the red, green, and blue components. The `red`, `green`, and `blue` components have a nominal range of [0..1], `exposure` is a value >= 0. To produce an HDR color, we process the given color in a linear color space, multiplying component values by `2^exposure`. The produced color will have a `contentHeadroom` equal to the linearized exposure value. Each whole value of exposure produces a color that is twice as bright.
### Creating a pattern-based color
- [init(patternImage: NSImage)](./nscolor/init%28patternimage%29.md)
  Creates a color object that uses the specified image pattern to paint the target area.
- [var patternImage: NSImage](./nscolor/patternimage.md)
  The pattern image used to paint the target area.
### Creating a color dynamically
- [init(name: NSColor.Name?, dynamicProvider: (NSAppearance) -> NSColor)](./nscolor/init%28name,dynamicprovider%29.md)
  Creates a dynamic catalog color with a provider that’s used to resolve the exact color value, calculated on first use.
### Creating a color in an arbitrary color space
- [init(colorSpace: NSColorSpace, components: UnsafePointer<CGFloat>, count: Int)](./nscolor/init%28colorspace,components,count%29.md)
  Creates a color object from the specified components of the given color space.
### Creating a system tint color
- [enum NSControlTint](./nscontroltint.md)
  Constants for specifying a cell’s tint color.
- [init(for: NSControlTint)](./nscolor/init%28for%29.md)
  Returns the color object specified by the given control tint.
### Converting other types of color objects
- [convenience init(Color)](./nscolor/init%28_%29.md)
- [init?(cgColor: CGColor)](./nscolor/init%28cgcolor%29-1hzl8.md)
  Creates a color object using the specified Core Graphics color.
- [init(CIColor: CIColor)](./nscolor/init%28cicolor%29-3rxsk.md)
  Creates a color object from the specified Core Image color.
### Creating color objects
- [init()](./nscolor/init%28%29.md)
  Initializes the color object.
- [init?(coder: NSCoder)](./nscolor/init%28coder%29.md)
  Creates a color object from data in an unarchiver.
- [convenience init(resource: ColorResource)](./nscolor/init%28resource%29.md)
  Initialize a `NSColor` with a color resource.

## See Also

### Getting and creating colors
- [UI element colors](./ui-element-colors.md)
  Retrieve standard color objects for use with windows, controls, labels, text, selections and other content in your app.
- [Standard colors](./standard-colors.md)
  Retrieve the standard color objects for common colors like red, blue, green, black, white, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/color-creation)*