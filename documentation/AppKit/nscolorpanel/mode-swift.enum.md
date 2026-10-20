# NSColorPanel.Mode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A type defined for the `enum` constants specifying color panel modes.

**Availability**:
- macOS

## Declaration

```swift
enum Mode
```

```c
enum NSColorPanelMode : NSInteger;
```

## Topics

### Color Panel Modes
- [NSColorPanel.Mode.none](./mode-swift.enum/none.md)
  No color panel mode.
- [NSColorPanel.Mode.gray](./mode-swift.enum/gray.md)
  The grayscale-alpha color mode.
- [NSColorPanel.Mode.RGB](./mode-swift.enum/rgb.md)
  The red-green-blue color mode.
- [NSColorPanel.Mode.CMYK](./mode-swift.enum/cmyk.md)
  The cyan-magenta-yellow-black color mode.
- [NSColorPanel.Mode.HSB](./mode-swift.enum/hsb.md)
  The hue-saturation-brightness color mode.
- [NSColorPanel.Mode.customPalette](./mode-swift.enum/custompalette.md)
  The custom palette color mode.
- [NSColorPanel.Mode.colorList](./mode-swift.enum/colorlist.md)
  The custom color list mode.
- [NSColorPanel.Mode.wheel](./mode-swift.enum/wheel.md)
  The color wheel mode.
- [NSColorPanel.Mode.crayon](./mode-swift.enum/crayon.md)
  The crayon picker mode.
### Deprecated
- [Deprecated symbols](../mode-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting color picker modes
- [class func setPickerMode(NSColorPanel.Mode)](./setpickermode%28_%29.md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](./mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [class func setPickerMask(NSColorPanel.Options)](./setpickermask%28_%29.md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](./options.md)
  The color modes that are enabled for a color panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/mode-swift.enum)*