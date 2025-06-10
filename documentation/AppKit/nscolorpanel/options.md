# NSColorPanel.Options

**Framework**: AppKit  
**Kind**: struct

The color modes that are enabled for a color panel.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Options
```

## Topics

### Color Panel Options
- [static var grayModeMask: NSColorPanel.Options](nscolorpanel/options/graymodemask.md)
  The grayscale-alpha color mode.
- [static var rgbModeMask: NSColorPanel.Options](nscolorpanel/options/rgbmodemask.md)
  The red-green-blue color mode.
- [static var cmykModeMask: NSColorPanel.Options](nscolorpanel/options/cmykmodemask.md)
  The cyan-magenta-yellow-black color mode.
- [static var hsbModeMask: NSColorPanel.Options](nscolorpanel/options/hsbmodemask.md)
  The hue-saturation-brightness color mode.
- [static var customPaletteModeMask: NSColorPanel.Options](nscolorpanel/options/custompalettemodemask.md)
  The custom palette color mode.
- [static var colorListModeMask: NSColorPanel.Options](nscolorpanel/options/colorlistmodemask.md)
  The custom color list mode.
- [static var wheelModeMask: NSColorPanel.Options](nscolorpanel/options/wheelmodemask.md)
  The color wheel mode.
- [static var crayonModeMask: NSColorPanel.Options](nscolorpanel/options/crayonmodemask.md)
  The crayon color mode.
- [static var allModesMask: NSColorPanel.Options](nscolorpanel/options/allmodesmask.md)
  All color modes.
### Initializers
- [init(rawValue: UInt)](nscolorpanel/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func setPickerMode(NSColorPanel.Mode)](nscolorpanel/setpickermode(_:).md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](nscolorpanel/mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](nscolorpanel/setpickermask(_:).md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/options)*