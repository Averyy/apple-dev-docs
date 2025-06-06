# NSColorPanel

**Framework**: AppKit  
**Kind**: class

A standard user interface for selecting color in an app.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSColorPanel
```

#### Overview

[`NSColorPanel`](nscolorpanel.md) provides a number of standard color selection modes and, with the [`NSColorPickingDefault`](nscolorpickingdefault.md) and [`NSColorPickingCustom`](nscolorpickingcustom.md) protocols, allows an app to add its own color selection modes. It also allows the user to save swatches containing frequently used colors.

## Topics

### Obtaining the Shared Color-Panel Object
- [class var shared: NSColorPanel](nscolorpanel/shared.md)
  Returns the shared `NSColorPanel` instance, creating it if necessary.
- [class var sharedColorPanelExists: Bool](nscolorpanel/sharedcolorpanelexists.md)
  Returns  a Boolean value indicating whether the `NSColorPanel` has been created already.
### Setting Color Picker Modes
- [class func setPickerMode(NSColorPanel.Mode)](nscolorpanel/setpickermode(_:).md)
  Specifies the color panel’s initial picker.
- [var mode: NSColorPanel.Mode](nscolorpanel/mode-swift.property.md)
  The mode of the receiver the mode is one of the modes allowed by the color mask.
- [NSColorPanel.Mode](nscolorpanel/mode-swift.enum.md)
  A type defined for the `enum` constants specifying color panel modes.
- [class func setPickerMask(NSColorPanel.Options)](nscolorpanel/setpickermask(_:).md)
  Determines which color selection modes are available in an application’s `NSColorPanel`.
- [NSColorPanel.Options](nscolorpanel/options.md)
  The color modes that are enabled for a color panel.
### Configuring the Color Panel
- [var accessoryView: NSView?](nscolorpanel/accessoryview.md)
  The accessory view.
- [var isContinuous: Bool](nscolorpanel/iscontinuous.md)
  A Boolean value indicating whether the receiver continuously sends the action message to the target.
- [func setAction(Selector?)](nscolorpanel/setaction(_:).md)
  Sets the color panel’s action message.
- [func setTarget(Any?)](nscolorpanel/settarget(_:).md)
  Sets the target of the receiver.
- [var showsAlpha: Bool](nscolorpanel/showsalpha.md)
  A Boolean value that indicates whether the receiver shows alpha values and an opacity slider.
### Managing Color Lists
- [func attachColorList(NSColorList)](nscolorpanel/attachcolorlist(_:).md)
  Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](nscolorpanel/attachcolorlist(_:).md) on all color pickers in the application.
- [func detachColorList(NSColorList)](nscolorpanel/detachcolorlist(_:).md)
  Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](nscolorpanel/detachcolorlist(_:).md) on all color pickers in the application.
### Setting Color
- [class func dragColor(NSColor, with: NSEvent, from: NSView) -> Bool](nscolorpanel/dragcolor(_:with:from:).md)
  Drags a color into a destination view from the specified source view.
- [var color: NSColor](nscolorpanel/color.md)
  The color of the receiver.
### Getting Transparency Information
- [var alpha: CGFloat](nscolorpanel/alpha.md)
  The receiver’s current alpha value based on its opacity slider.
### Responding to a Color Change
- [protocol NSColorChanging](nscolorchanging.md)
- [class let colorDidChangeNotification: NSNotification.Name](nscolorpanel/colordidchangenotification.md)
  Posted when the color of the `NSColorPanel` is set, as when [`NSColorPanel`](nscolorpanel.md) is invoked.

## Relationships

### Inherits From
- [NSPanel](nspanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSColorPickingCustom](nscolorpickingcustom.md)
  A set of methods that provides a way to add color pickers—custom user interfaces for color selection—to an app’s color panel.
- [protocol NSColorPickingDefault](nscolorpickingdefault.md)
  A set of methods that provides basic behavior for a color picker.
- [class NSColorPicker](nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel)*