# NSColorWell

**Framework**: AppKit  
**Kind**: class

A control that displays a color value and lets the user change that color value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSColorWell
```

#### Overview

An [`NSColorWell`](nscolorwell.md) object lets people select colors from your interface. Incorporate this type of control if your app supports custom color selection. For example, a drawing app might include a color well to let someone choose the color to use when drawing. A color well control displays the currently selected color, and interactions with the color well display interfaces for selecting new colors.

When you create a color well programmatically or in Interface Builder, specify the appearance and interaction style you want. The color well supports color selection using a color picker popover or the system [`NSColorPanel`](nscolorpanel.md) object. When someone selects a new color in one of these interfaces, the color well updates its selected color to match. You can also provide your own color selection process using a custom action and update the color yourself.

## Topics

### Creating a Color Well
- [convenience init(style: NSColorWell.Style)](nscolorwell/init(style:).md)
  Creates a color well that adopts the specified appearance style.
### Managing the Selected Color
- [var color: NSColor](nscolorwell/color.md)
  The currently selected color for the color well.
- [func takeColorFrom(Any?)](nscolorwell/takecolorfrom(_:).md)
  Changes the currently selected color to the color of the specified object.
- [var supportsAlpha: Bool](nscolorwell/supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.
### Configuring the Appearance
- [var colorWellStyle: NSColorWell.Style](nscolorwell/colorwellstyle.md)
  The appearance and interaction style to apply to the color well.
- [NSColorWell.Style](nscolorwell/style.md)
  Constants that specify the appearance and interaction modes for a color well.
- [var image: NSImage?](nscolorwell/image.md)
  The image to display on the button portion of a color well that adopts the expanded style.
- [var isBordered: Bool](nscolorwell/isbordered.md)
  A Boolean value that determines whether the color well has a border.
### Activating and Deactivating Color Wells
- [func activate(Bool)](nscolorwell/activate(_:).md)
  Activates the color well, displays the color panel, and synchronizes the two UI elements.
- [var isActive: Bool](nscolorwell/isactive.md)
  A Boolean value that indicates whether the color well is currently active.
- [func deactivate()](nscolorwell/deactivate.md)
  Deactivates the color well.
### Drawing Color Wells
- [func drawWell(inside: NSRect)](nscolorwell/drawwell(inside:).md)
  Draws the area inside the color well at the specified location without drawing borders.
### Customizing the Color Selection Behavior
- [var pulldownAction: Selector?](nscolorwell/pulldownaction.md)
  The action to perform when someone clicks in the color area of the color well.
- [var pulldownTarget: AnyObject?](nscolorwell/pulldowntarget.md)
  The target object that defines the action you want to perform when someone interacts with the color well.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
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
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSColorPicker](nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell)*