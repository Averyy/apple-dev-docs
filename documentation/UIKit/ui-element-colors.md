# UI element colors

**Framework**: UIKit

Choose colors for UI elements such as labels, text, backgrounds, and links.

#### Overview

UIKit provides color objects for the foreground and background colors of your app’s UI elements. The names of these color objects reflect their intended use, rather than specific color values.

Except where noted, the color objects adapt automatically to Dark Mode changes when you use the provided [`UIColor`](uicolor.md) object. If you retrieve the color values, either directly or using another type such as [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor), you must handle Dark Mode changes yourself. For more information about supporting Dark Mode, see [`Supporting Dark Mode in your interface`](supporting-dark-mode-in-your-interface.md).

## Topics

### Label colors
- [class var label: UIColor](uicolor/label.md)
  The color for text labels that contain primary content.
- [class var secondaryLabel: UIColor](uicolor/secondarylabel.md)
  The color for text labels that contain secondary content.
- [class var tertiaryLabel: UIColor](uicolor/tertiarylabel.md)
  The color for text labels that contain tertiary content.
- [class var quaternaryLabel: UIColor](uicolor/quaternarylabel.md)
  The color for text labels that contain quaternary content.
### Fill colors
- [class var systemFill: UIColor](uicolor/systemfill.md)
  An overlay fill color for thin and small shapes.
- [class var secondarySystemFill: UIColor](uicolor/secondarysystemfill.md)
  An overlay fill color for medium-size shapes.
- [class var tertiarySystemFill: UIColor](uicolor/tertiarysystemfill.md)
  An overlay fill color for large shapes.
- [class var quaternarySystemFill: UIColor](uicolor/quaternarysystemfill.md)
  An overlay fill color for large areas that contain complex content.
### Text colors
- [class var placeholderText: UIColor](uicolor/placeholdertext.md)
  The color for placeholder text in controls or text views.
### Tint color
- [class var tintColor: UIColor](uicolor/tintcolor.md)
  A color value that resolves at runtime based on the current tint color of the app or trait hierarchy.
### Standard content background colors
- [class var systemBackground: UIColor](uicolor/systembackground.md)
  The color for the main background of your interface.
- [class var secondarySystemBackground: UIColor](uicolor/secondarysystembackground.md)
  The color for content layered on top of the main background.
- [class var tertiarySystemBackground: UIColor](uicolor/tertiarysystembackground.md)
  The color for content layered on top of secondary backgrounds.
### Grouped content background colors
- [class var systemGroupedBackground: UIColor](uicolor/systemgroupedbackground.md)
  The color for the main background of your grouped interface.
- [class var secondarySystemGroupedBackground: UIColor](uicolor/secondarysystemgroupedbackground.md)
  The color for content layered on top of the main background of your grouped interface.
- [class var tertiarySystemGroupedBackground: UIColor](uicolor/tertiarysystemgroupedbackground.md)
  The color for content layered on top of secondary backgrounds of your grouped interface.
### Separator colors
- [class var separator: UIColor](uicolor/separator.md)
  The color for thin borders or divider lines that allows some underlying content to be visible.
- [class var opaqueSeparator: UIColor](uicolor/opaqueseparator.md)
  The color for borders or divider lines that hides any underlying content.
### Link color
- [class var link: UIColor](uicolor/link.md)
  The specified color for links.
### Nonadaptable colors
- [class var darkText: UIColor](uicolor/darktext.md)
  The nonadaptable system color for text on a light background.
- [class var lightText: UIColor](uicolor/lighttext.md)
  The nonadaptable system color for text on a dark background.
### Deprecated colors
- [class var groupTableViewBackground: UIColor](uicolor/grouptableviewbackground.md)
  The system color to use for the background of a grouped table.

## See Also

- [Standard colors](standard-colors.md)
  Define standard color objects for specific shades, such as red, blue, green, black, white, and more.
- [Color creation](color-creation.md)
  Load colors from asset catalogs and create colors from raw component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/ui-element-colors)*