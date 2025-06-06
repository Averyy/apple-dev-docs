# Standard colors

**Framework**: UIKit

Define standard color objects for specific shades, such as red, blue, green, black, white, and more.

#### Overview

Use the standard color objects when you want to use a specific color shade in your UI. To view swatches of these colors, see [`System Colors`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/#system-colors).

The system color objects adapt automatically to Dark Mode changes when you use the provided [`UIColor`](uicolor.md) object, but the fixed-shade colors don’t adapt. If you retrieve the color values, either directly or using another type such as [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor), you must handle Dark Mode changes yourself. For more information about supporting Dark Mode, see [`Supporting Dark Mode in your interface`](supporting-dark-mode-in-your-interface.md).

## Topics

### Adaptable colors
- [class var systemBlue: UIColor](uicolor/systemblue.md)
  A blue color that automatically adapts to the current trait environment.
- [class var systemBrown: UIColor](uicolor/systembrown.md)
  A brown color that automatically adapts to the current trait environment.
- [class var systemCyan: UIColor](uicolor/systemcyan.md)
  A cyan color that automatically adapts to the current trait environment.
- [class var systemGreen: UIColor](uicolor/systemgreen.md)
  A green color that automatically adapts to the current trait environment.
- [class var systemIndigo: UIColor](uicolor/systemindigo.md)
  An indigo color that automatically adapts to the current trait environment.
- [class var systemMint: UIColor](uicolor/systemmint.md)
  A mint color that automatically adapts to the current trait environment.
- [class var systemOrange: UIColor](uicolor/systemorange.md)
  An orange color that automatically adapts to the current trait environment.
- [class var systemPink: UIColor](uicolor/systempink.md)
  A pink color that automatically adapts to the current trait environment.
- [class var systemPurple: UIColor](uicolor/systempurple.md)
  A purple color that automatically adapts to the current trait environment.
- [class var systemRed: UIColor](uicolor/systemred.md)
  A red color that automatically adapts to the current trait environment.
- [class var systemTeal: UIColor](uicolor/systemteal.md)
  A teal color that automatically adapts to the current trait environment.
- [class var systemYellow: UIColor](uicolor/systemyellow.md)
  A yellow color that automatically adapts to the current trait environment.
### Adaptable gray colors
- [class var systemGray: UIColor](uicolor/systemgray.md)
  The standard base gray color that adapts to the environment.
- [class var systemGray2: UIColor](uicolor/systemgray2.md)
  A second-level shade of gray that adapts to the environment.
- [class var systemGray3: UIColor](uicolor/systemgray3.md)
  A third-level shade of gray that adapts to the environment.
- [class var systemGray4: UIColor](uicolor/systemgray4.md)
  A fourth-level shade of gray that adapts to the environment.
- [class var systemGray5: UIColor](uicolor/systemgray5.md)
  A fifth-level shade of gray that adapts to the environment.
- [class var systemGray6: UIColor](uicolor/systemgray6.md)
  A sixth-level shade of gray that adapts to the environment.
### Transparent color
- [class var clear: UIColor](uicolor/clear.md)
  A color object with grayscale and alpha values that are both `0.0`.
### Fixed colors
- [class var black: UIColor](uicolor/black.md)
  A color object in the sRGB color space with a grayscale value of `0.0` and an alpha value of `1.0`.
- [class var blue: UIColor](uicolor/blue.md)
  A color object with RGB values of `0.0`, `0.0`, and `1.0`, and an alpha value of `1.0`.
- [class var brown: UIColor](uicolor/brown.md)
  A color object with RGB values of `0.6`, `0.4`, and `0.2`, and an alpha value of `1.0`.
- [class var cyan: UIColor](uicolor/cyan.md)
  A color object with RGB values of `0.0`, `1.0`, and `1.0`, and an alpha value of `1.0`.
- [class var darkGray: UIColor](uicolor/darkgray.md)
  A color object with a grayscale value of 1/3 and an alpha value of `1.0`.
- [class var gray: UIColor](uicolor/gray.md)
  A color object with a grayscale value of `0.5` and an alpha value of `1.0`.
- [class var green: UIColor](uicolor/green.md)
  A color object with RGB values of `0.0`, `1.0`, and `0.0`, and an alpha value of `1.0`.
- [class var lightGray: UIColor](uicolor/lightgray.md)
  A color object with a grayscale value of 2/3 and an alpha value of `1.0`.
- [class var magenta: UIColor](uicolor/magenta.md)
  A color object with RGB values of `1.0`, `0.0`, and `1.0`, and an alpha value of `1.0`.
- [class var orange: UIColor](uicolor/orange.md)
  A color object with RGB values of `1.0`, `0.5`, and `0.0`, and an alpha value of `1.0`.
- [class var purple: UIColor](uicolor/purple.md)
  A color object with RGB values of `0.5`, `0.0`, and `0.5`, and an alpha value of `1.0`.
- [class var red: UIColor](uicolor/red.md)
  A color object with RGB values of `1.0`, `0.0`, and `0.0`, and an alpha value of `1.0`.
- [class var white: UIColor](uicolor/white.md)
  A color object with a grayscale value of `1.0` and an alpha value of `1.0`.
- [class var yellow: UIColor](uicolor/yellow.md)
  A color object with RGB values of `1.0`, `1.0`, and `0.0`, and an alpha value of `1.0`.

## See Also

- [UI element colors](ui-element-colors.md)
  Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Color creation](color-creation.md)
  Load colors from asset catalogs and create colors from raw component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/standard-colors)*