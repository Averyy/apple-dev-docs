# NSColorPickingCustom

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that provides a way to add color pickers—custom user interfaces for color selection—to an app’s color panel.

**Availability**:
- macOS

## Declaration

```swift
protocol NSColorPickingCustom : NSColorPickingDefault
```

```objc
@protocol NSColorPickingCustom <NSColorPickingDefault>
```

## Overview

[`NSColorPickingCustom`](./nscolorpickingcustom.md) works with the [`NSColorPickingDefault`](./nscolorpickingdefault.md) protocol—which provides basic behavior for a color picker—to enable custom color pickers.

> **Note**:  This protocol must be implemented by a custom picker, or an error will occur.

## Topics

### Configuring Color Pickers
- [func setColor(NSColor)](./nscolorpickingcustom/setcolor%28_%29.md)
  Adjusts the receiver to make the specified color the currently selected color.
### Getting Color Picker Information
- [func currentMode() -> NSColorPanel.Mode](./nscolorpickingcustom/currentmode%28%29.md)
  Returns the receiver’s current mode (or submode, if applicable).
- [func supportsMode(NSColorPanel.Mode) -> Bool](./nscolorpickingcustom/supportsmode%28_%29.md)
  Returns a Boolean value indicating whether or not the receiver supports the specified picking mode.
### Displaying Color Pickers
- [func provideNewView(Bool) -> NSView](./nscolorpickingcustom/providenewview%28_%29.md)
  Returns the view containing the receiver’s user interface.

## Relationships

### Inherits From
- [NSColorPickingDefault](./nscolorpickingdefault.md)

## See Also

### Color Panels
- [class NSColorPanel](./nscolorpanel.md)
  A standard user interface for selecting color in an app.
- [protocol NSColorPickingDefault](./nscolorpickingdefault.md)
  A set of methods that provides basic behavior for a color picker.
- [class NSColorPicker](./nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom)*