# NSColorPanel.Mode

**Framework**: AppKit  
**Kind**: enum

A type defined for the `enum` constants specifying color panel modes.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Mode
```

## Topics

### Color Panel Modes
- [NSColorPanel.Mode.none](nscolorpanel/mode-swift.enum/none.md)
  No color panel mode.
- [NSColorPanel.Mode.gray](nscolorpanel/mode-swift.enum/gray.md)
  The grayscale-alpha color mode.
- [NSColorPanel.Mode.RGB](nscolorpanel/mode-swift.enum/rgb.md)
  The red-green-blue color mode.
- [NSColorPanel.Mode.CMYK](nscolorpanel/mode-swift.enum/cmyk.md)
  The cyan-magenta-yellow-black color mode.
- [NSColorPanel.Mode.HSB](nscolorpanel/mode-swift.enum/hsb.md)
  The hue-saturation-brightness color mode.
- [NSColorPanel.Mode.customPalette](nscolorpanel/mode-swift.enum/custompalette.md)
  The custom palette color mode.
- [NSColorPanel.Mode.colorList](nscolorpanel/mode-swift.enum/colorlist.md)
  The custom color list mode.
- [NSColorPanel.Mode.wheel](nscolorpanel/mode-swift.enum/wheel.md)
  The color wheel mode.
- [NSColorPanel.Mode.crayon](nscolorpanel/mode-swift.enum/crayon.md)
  The crayon picker mode.
### Initializers
- [init?(rawValue: Int)](nscolorpanel/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func setPickerMode(NSColorPanel.Mode)](nscolorpanel/setpickermode(_:).md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [class func setPickerMask(NSColorPanel.Options)](nscolorpanel/setpickermask(_:).md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](nscolorpanel/options.md)
  The color modes that are enabled for a color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/mode-swift.enum)*