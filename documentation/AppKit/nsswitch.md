# NSSwitch

**Framework**: AppKit  
**Kind**: class

A control that offers a binary choice.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSSwitch
```

#### Overview

The [`NSSwitch`](nsswitch.md) class provides a simple interface for displaying and toggling a Boolean state, such as on/off. A switch toggles its [`state`](nsswitch/state.md) and sends its [`action`](nscontrol/action.md) when clicked, activated through the keyboard, or tapped in the Touch Bar. [`NSSwitch`](nsswitch.md) also allows dragging between states, and if [`isContinuous`](nscontrol/iscontinuous.md) is [`true`](https://developer.apple.com/documentation/swift/true), the switch sends its [`action`](nscontrol/action.md) for each change in position during the drag.

Use a switch to toggle significant preferences, or preferences that provide access to other controls. Avoid creating lists or tables of switches; instead, for general-purpose toggles, use an instance of [`NSButton`](nsbutton.md) to display a checkbox.

[`NSSwitch`](nsswitch.md) doesn’t use an instance of [`NSCell`](nscell.md) to provide its functionality. The [`cellClass`](nscontrol/cellclass.md) class property and [`cell`](nscontrol/cell.md) instance property both return [`Nil`](https://developer.apple.com/documentation/objectivec/nil), and they ignore attempts to set a non-[`Nil`](https://developer.apple.com/documentation/objectivec/nil) value.

## Topics

### Managing Switch State
- [var state: NSControl.StateValue](nsswitch/state.md)
  The current position of the switch.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityButton](nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilitySwitch](nsaccessibilityswitch.md)
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

## See Also

- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsswitch)*