# NSStepper

**Framework**: AppKit  
**Kind**: class

An interface with up and down arrow buttons for incrementing or decrementing a value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSStepper
```

#### Overview

A stepper consists of two small arrows that can increment and decrement a value that appears beside it, such as a date or time. The illustration below shows a stepper to the right of a text field, which would show the stepper’s value.

![None](https://docs-assets.developer.apple.com/published/01e47ff4595b41b2c127100c1748260e/media-2555815%402x.png)

The `NSStepper` class uses the [`NSStepperCell`](nssteppercell.md) class to implement its user interface.

## Topics

### Configuring the Cell
- [class NSStepperCell](nssteppercell.md)
  An `NSStepperCell` object controls the appearance and behavior of an [`NSStepper`](nsstepper.md) object.
### Specifying value range
- [var maxValue: Double](nsstepper/maxvalue.md)
  The stepper’s maximum value.
- [var minValue: Double](nsstepper/minvalue.md)
  The stepper’s minimum value.
- [var increment: Double](nsstepper/increment.md)
  The amount by which the receiver changes with each increment or decrement.
### Specifying how the stepper responds
- [var autorepeat: Bool](nsstepper/autorepeat.md)
  A Boolean value that indicates how the stepper responds to mouse events.
- [var valueWraps: Bool](nsstepper/valuewraps.md)
  A Boolean value that indicates whether the stepper wraps around the minimum and maximum values.

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
- [NSAccessibilityStepper](nsaccessibilitystepper.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstepper)*