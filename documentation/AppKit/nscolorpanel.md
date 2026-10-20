# NSColorPanel

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A standard user interface for selecting color in an app.

**Availability**:
- macOS

## Declaration

```swift
class NSColorPanel
```

```objc
@interface NSColorPanel : NSPanel
```

#### Overview

[`NSColorPanel`](./nscolorpanel.md) provides a number of standard color selection modes and, with the [`NSColorPickingDefault`](./nscolorpickingdefault.md) and [`NSColorPickingCustom`](./nscolorpickingcustom.md) protocols, allows an app to add its own color selection modes. It also allows the user to save swatches containing frequently used colors.

## Topics

### Obtaining the shared color panel
- [class var shared: NSColorPanel](./nscolorpanel/shared.md)
  Returns the shared `NSColorPanel` instance, creating it if necessary.
- [class var sharedColorPanelExists: Bool](./nscolorpanel/sharedcolorpanelexists.md)
  Returns  a Boolean value indicating whether the `NSColorPanel` has been created already.
### Setting color picker modes
- [class func setPickerMode(NSColorPanel.Mode)](./nscolorpanel/setpickermode%28_%29.md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](./nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](./nscolorpanel/mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](./nscolorpanel/setpickermask%28_%29.md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](./nscolorpanel/options.md)
  The color modes that are enabled for a color panel.
### Configuring the color panel
- [var accessoryView: NSView?](./nscolorpanel/accessoryview.md)
  The accessory view.
- [var isContinuous: Bool](./nscolorpanel/iscontinuous.md)
  A Boolean value indicating whether the receiver continuously sends the action message to the target.
- [func setAction(Selector?)](./nscolorpanel/setaction%28_%29.md)
  Sets the color panel’s action message.
- [func setTarget(Any?)](./nscolorpanel/settarget%28_%29.md)
  Sets the target of the receiver.
- [var showsAlpha: Bool](./nscolorpanel/showsalpha.md)
  A Boolean value that indicates whether the receiver shows alpha values and an opacity slider.
### Managing color lists
- [func attachColorList(NSColorList)](./nscolorpanel/attachcolorlist%28_%29.md)
  Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](./nscolorpanel/attachcolorlist%28_%29.md) on all color pickers in the application.
- [func detachColorList(NSColorList)](./nscolorpanel/detachcolorlist%28_%29.md)
  Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](./nscolorpanel/detachcolorlist%28_%29.md) on all color pickers in the application.
### Setting color
- [class func dragColor(NSColor, with: NSEvent, from: NSView) -> Bool](./nscolorpanel/dragcolor%28_,with,from%29.md)
  Drags a color into a destination view from the specified source view.
- [var color: NSColor](./nscolorpanel/color.md)
  The color of the receiver.
### Supporting high dynamic range (HDR) colors
- [var maximumLinearExposure: CGFloat](./nscolorpanel/maximumlinearexposure.md)
  The maximum linear exposure that can be set on a color picked in the color panel. Defaults to 1 and ignores any value less than 1. If set to a value >= 2, the color picked by the panel may have a linear exposure applied to it.
### Getting transparency information
- [var alpha: CGFloat](./nscolorpanel/alpha.md)
  The receiver’s current alpha value based on its opacity slider.
### Responding to a color change
- [protocol NSColorChanging](./nscolorchanging.md)
- [class let colorDidChangeNotification: NSNotification.Name](./nscolorpanel/colordidchangenotification.md)
  Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](./nscolorpanel.md) is invoked.
### Structures
- [NSColorPanel.ColorDidChangeMessage](./nscolorpanel/colordidchangemessage.md)

## Relationships

### Inherits From
- [NSPanel](./nspanel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSMenuItemValidation](./nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](./nsuserinterfacevalidations.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Color Panels
- [protocol NSColorPickingCustom](./nscolorpickingcustom.md)
  A set of methods that provides a way to add color pickers—custom user interfaces for color selection—to an app’s color panel.
- [protocol NSColorPickingDefault](./nscolorpickingdefault.md)
  A set of methods that provides basic behavior for a color picker.
- [class NSColorPicker](./nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel)*