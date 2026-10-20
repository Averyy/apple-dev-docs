# NSProgressIndicator

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An interface that provides visual feedback to the user about the status of an ongoing task.

**Availability**:
- macOS

## Declaration

```swift
class NSProgressIndicator
```

```objc
@interface NSProgressIndicator : NSView
```

#### Overview

Progress indicators can be determinate or indeterminate. A determinate indicator displays the completion percentage of a task. An indeterminate indicator shows that the app is busy without providing a visual indication of how long the task will take.

## Topics

### Animating the progress indicator
- [func startAnimation(Any?)](./nsprogressindicator/startanimation%28_%29.md)
  Starts the animation of an indeterminate progress indicator.
- [func stopAnimation(Any?)](./nsprogressindicator/stopanimation%28_%29.md)
  Stops the animation of an indeterminate progress indicator.
- [var usesThreadedAnimation: Bool](./nsprogressindicator/usesthreadedanimation.md)
  A Boolean that indicates whether the progress indicator implements animation in a separate thread.
### Advancing the progress bar
- [func increment(by: Double)](./nsprogressindicator/increment%28by%29.md)
  Advances the progress bar of a determinate progress indicator by the specified amount.
- [var doubleValue: Double](./nsprogressindicator/doublevalue.md)
  The value that indicates the current extent of the progress indicator.
- [var minValue: Double](./nsprogressindicator/minvalue.md)
  The minimum value for the progress indicator.
- [var maxValue: Double](./nsprogressindicator/maxvalue.md)
  The maximum value for the progress indicator.
### Observing the progress bar
- [var observedProgress: Progress?](./nsprogressindicator/observedprogress.md)
  The progress object to use for updating the progress view.
### Setting the appearance
- [var controlSize: NSControl.ControlSize](./nsprogressindicator/controlsize.md)
  The size of the progress indicator.
- [var isIndeterminate: Bool](./nsprogressindicator/isindeterminate.md)
  A Boolean that indicates whether the progress indicator is indeterminate.
- [var style: NSProgressIndicator.Style](./nsprogressindicator/style-swift.property.md)
  The style of the progress indicator (bar or spinning).
- [func sizeToFit()](./nsprogressindicator/sizetofit%28%29.md)
  This action method resizes the progress indicator to an appropriate size depending on the value of [`style`](./nsprogressindicator/style-swift.property.md).
- [var isDisplayedWhenStopped: Bool](./nsprogressindicator/isdisplayedwhenstopped.md)
  A Boolean that indicates whether the progress indicator hides itself when it isn’t animating.
### Constants
- [NSProgressIndicator.Style](./nsprogressindicator/style-swift.enum.md)
  Constants that specify the progress indicator’s style.
### Deprecated
- [Deprecated symbols](./nsprogressindicator-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSView](./nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](./nsaccessibilitygroup.md)
- [NSAccessibilityProgressIndicator](./nsaccessibilityprogressindicator.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controls
- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](./nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](./nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](./combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](./nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](./date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](./nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](./nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](./path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](./nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSRuleEditor](./nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](./nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](./search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](./nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](./slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator)*