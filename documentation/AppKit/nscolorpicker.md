# NSColorPicker

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract superclass that implements the default color picking protocol.

**Availability**:
- macOS

## Declaration

```swift
class NSColorPicker
```

```objc
@interface NSColorPicker : NSObject
```

#### Overview

The [`NSColorPickingDefault`](./nscolorpickingdefault.md) and [`NSColorPickingCustom`](./nscolorpickingcustom.md) protocols define a way to add color pickers (custom user interfaces for color selection) to the color panel.

## Topics

### Initializing the Color Picker Object
- [init?(pickerMask: Int, colorPanel: NSColorPanel)](./nscolorpicker/init%28pickermask,colorpanel%29.md)
  Initializes the color picker with the specified color panel and color picker mode mask.
### Getting the Color Panel
- [var colorPanel: NSColorPanel](./nscolorpicker/colorpanel.md)
  The color panel instance that owns the color picker.
### Adding Button Images
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./nscolorpicker/insertnewbuttonimage%28_,in%29.md)
  Sets the image used for the specified button cell.
- [var provideNewButtonImage: NSImage](./nscolorpicker/providenewbuttonimage.md)
  The button image used by the color picker.
### Setting the Mode
- [func setMode(NSColorPanel.Mode)](./nscolorpicker/setmode%28_%29.md)
  Overriden to set the color picker’s mode.
### Managing Color Lists
- [func attachColorList(NSColorList)](./nscolorpicker/attachcolorlist%28_%29.md)
  Overriden to attach a color list to a color picker.
- [func detachColorList(NSColorList)](./nscolorpicker/detachcolorlist%28_%29.md)
  Overriden to detach a color list from a color picker.
### Responding to View Changes
- [func viewSizeChanged(Any?)](./nscolorpicker/viewsizechanged%28_%29.md)
  Overriden to respond to a size change.
### Customizing the Color Picker
- [var buttonToolTip: String](./nscolorpicker/buttontooltip.md)
  The tool tip that is shown when the mouse cursor is over the color picker’s button image.
- [var minContentSize: NSSize](./nscolorpicker/mincontentsize.md)
  The minimum content size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSColorPickingDefault](./nscolorpickingdefault.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Color Selection
- [class NSColorWell](./nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [class NSColorPickerTouchBarItem](./nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpicker)*