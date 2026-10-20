# NSColorPanel.Options

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The color modes that are enabled for a color panel.

**Availability**:
- macOS

## Declaration

```swift
struct Options
```

```c
enum NSColorPanelOptions : NSUInteger;
```

## Topics

### Color Panel Options
- [static var grayModeMask: NSColorPanel.Options](./options/graymodemask.md)
  The grayscale-alpha color mode.
- [static var rgbModeMask: NSColorPanel.Options](./options/rgbmodemask.md)
  The red-green-blue color mode.
- [static var cmykModeMask: NSColorPanel.Options](./options/cmykmodemask.md)
  The cyan-magenta-yellow-black color mode.
- [static var hsbModeMask: NSColorPanel.Options](./options/hsbmodemask.md)
  The hue-saturation-brightness color mode.
- [static var customPaletteModeMask: NSColorPanel.Options](./options/custompalettemodemask.md)
  The custom palette color mode.
- [static var colorListModeMask: NSColorPanel.Options](./options/colorlistmodemask.md)
  The custom color list mode.
- [static var wheelModeMask: NSColorPanel.Options](./options/wheelmodemask.md)
  The color wheel mode.
- [static var crayonModeMask: NSColorPanel.Options](./options/crayonmodemask.md)
  The crayon color mode.
- [static var allModesMask: NSColorPanel.Options](./options/allmodesmask.md)
  All color modes.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Setting color picker modes
- [class func setPickerMode(NSColorPanel.Mode)](./setpickermode%28_%29.md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](./mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](./mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](./setpickermask%28_%29.md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/options)*