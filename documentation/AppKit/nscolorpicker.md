# NSColorPicker

**Framework**: AppKit  
**Kind**: class

An abstract superclass that implements the default color picking protocol.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSColorPicker
```

#### Overview

The [`NSColorPickingDefault`](nscolorpickingdefault.md) and [`NSColorPickingCustom`](nscolorpickingcustom.md) protocols define a way to add color pickers (custom user interfaces for color selection) to the color panel.

## Topics

### Initializing the Color Picker Object
- [init?(pickerMask: Int, colorPanel: NSColorPanel)](nscolorpicker/init(pickermask:colorpanel:).md)
  Initializes the color picker with the specified color panel and color picker mode mask.
### Getting the Color Panel
- [var colorPanel: NSColorPanel](nscolorpicker/colorpanel.md)
  The color panel instance that owns the color picker.
### Adding Button Images
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](nscolorpicker/insertnewbuttonimage(_:in:).md)
  Sets the image used for the specified button cell.
- [var provideNewButtonImage: NSImage](nscolorpicker/providenewbuttonimage.md)
  The button image used by the color picker.
### Setting the Mode
- [func setMode(NSColorPanel.Mode)](nscolorpicker/setmode(_:).md)
  Overriden to set the color picker’s mode.
### Managing Color Lists
- [func attachColorList(NSColorList)](nscolorpicker/attachcolorlist(_:).md)
  Overriden to attach a color list to a color picker.
- [func detachColorList(NSColorList)](nscolorpicker/detachcolorlist(_:).md)
  Overriden to detach a color list from a color picker.
### Responding to View Changes
- [func viewSizeChanged(Any?)](nscolorpicker/viewsizechanged(_:).md)
  Overriden to respond to a size change.
### Customizing the Color Picker
- [var buttonToolTip: String](nscolorpicker/buttontooltip.md)
  The tool tip that is shown when the mouse cursor is over the color picker’s button image.
- [var minContentSize: NSSize](nscolorpicker/mincontentsize.md)
  The minimum content size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSColorPickingDefault](nscolorpickingdefault.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker)*