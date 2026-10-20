# NSColorPickingDefault

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that provides basic behavior for a color picker.

**Availability**:
- macOS

## Declaration

```swift
protocol NSColorPickingDefault
```

```objc
@protocol NSColorPickingDefault
```

#### Overview

The [`NSColorPickingDefault`](./nscolorpickingdefault.md) protocol, together with the [`NSColorPickingCustom`](./nscolorpickingcustom.md) protocol (which provides implementation-specific behavior), provides an interface for adding color pickers to an app’s color panel.

## Topics

### Creating Color Pickers
- [init?(pickerMask: Int, colorPanel: NSColorPanel)](./nscolorpickingdefault/init%28pickermask,colorpanel%29.md)
  Initializes the receiver with a given color panel and its mode.
### Configuring Color Pickers
- [func setMode(NSColorPanel.Mode)](./nscolorpickingdefault/setmode%28_%29.md)
  Specifies the receiver’s mode.
- [func insertNewButtonImage(NSImage, in: NSButtonCell)](./nscolorpickingdefault/insertnewbuttonimage%28_,in%29.md)
  Sets the image of a given button cell.
- [func provideNewButtonImage() -> NSImage](./nscolorpickingdefault/providenewbuttonimage%28%29.md)
  Provides the image of the button used to select the receiver in the color panel.
- [func minContentSize() -> NSSize](./nscolorpickingdefault/mincontentsize%28%29.md)
  Indicates the receiver’s minimum content size.
- [func buttonToolTip() -> String](./nscolorpickingdefault/buttontooltip%28%29.md)
  Provides the toolbar button help tag.
### Handling Events
- [func alphaControlAddedOrRemoved(Any?)](./nscolorpickingdefault/alphacontroladdedorremoved%28_%29.md)
  Sent when the color panel’s opacity controls have been hidden or displayed.
- [func viewSizeChanged(Any?)](./nscolorpickingdefault/viewsizechanged%28_%29.md)
  Tells the recever when the color panel’s view size changes in a way that might affect the color picker.
### Managing Color Lists
- [func attachColorList(NSColorList)](./nscolorpickingdefault/attachcolorlist%28_%29.md)
  Tells the receiver to attach the given color list, if it isn’t already displaying the list.
- [func detachColorList(NSColorList)](./nscolorpickingdefault/detachcolorlist%28_%29.md)
  Tells the receiver to detach the given color list, unless the receiver isn’t displaying the list.

## Relationships

### Inherited By
- [NSColorPickingCustom](./nscolorpickingcustom.md)
### Conforming Types
- [NSColorPicker](./nscolorpicker.md)

## See Also

### Color Panels
- [class NSColorPanel](./nscolorpanel.md)
  A standard user interface for selecting color in an app.
- [protocol NSColorPickingCustom](./nscolorpickingcustom.md)
  A set of methods that provides a way to add color pickers—custom user interfaces for color selection—to an app’s color panel.
- [class NSColorPicker](./nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault)*