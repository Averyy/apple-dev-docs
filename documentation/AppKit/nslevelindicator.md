# NSLevelIndicator

**Framework**: AppKit  
**Kind**: class

A visual representation of a level or quantity, using discrete values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSLevelIndicator
```

#### Overview

A level indicator is similar to an [`NSSlider`](nsslider.md) object, but provides a more customized visual feedback to the user. Unlike sliders, level indicators do not have a “knob” indicating the current setting, and they do not allow the user to adjust the current setting. You set the value of the level indicator programmatically. The supported indicator styles include:

- A capacity style level indicator. The continuous mode for this style is often used to indicate conditions such as how much data is on hard disk. The discrete mode is similar to audio level indicators in audio playback applications. You can specify both a warning value and a critical value that provides additional visual feedback to the user.
- A ranking style level indicator. This is similar to the star ranking displays provided in iTunes and iPhoto. You can also specify your own ranking image.
- A relevancy style level indicator. This style is used to display the relevancy of a search result, for example in Mail.

`NSLevelIndicator` uses an [`NSLevelIndicatorCell`](nslevelindicatorcell.md) to implement much of the control’s functionality. `NSLevelIndicator` provides cover methods for most of the [`NSLevelIndicatorCell`](nslevelindicatorcell.md) methods, which call the corresponding cell method.

## Topics

### Configuring the Cell
- [class NSLevelIndicatorCell](nslevelindicatorcell.md)
  `NSLevelIndicatorCell` is a subclass of [`NSActionCell`](nsactioncell.md) that provides several level indicator display styles including: capacity, ranking and relevancy. The capacity style provides both continuous and discrete modes.
### Configuring the Range of Values
- [var minValue: Double](nslevelindicator/minvalue.md)
  The receiver’s minimum value.
- [var maxValue: Double](nslevelindicator/maxvalue.md)
  The receiver’s maximum value.
- [var warningValue: Double](nslevelindicator/warningvalue.md)
  The receiver’s warning value.
- [var criticalValue: Double](nslevelindicator/criticalvalue.md)
  The receiver’s critical value.
### Managing Tick Marks and Style
- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicator/tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](nslevelindicator/numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [var numberOfMajorTickMarks: Int](nslevelindicator/numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](nslevelindicator/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicator/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicator/levelindicatorstyle.md)
  The appearance of the indicator.
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.
### Configuring the Drawing Attributes
- [var ratingImage: NSImage?](nslevelindicator/ratingimage.md)
- [var drawsTieredCapacityLevels: Bool](nslevelindicator/drawstieredcapacitylevels.md)
- [var fillColor: NSColor!](nslevelindicator/fillcolor.md)
- [var warningFillColor: NSColor!](nslevelindicator/warningfillcolor.md)
- [var criticalFillColor: NSColor!](nslevelindicator/criticalfillcolor.md)
### Managing Placeholder Information
- [var ratingPlaceholderImage: NSImage?](nslevelindicator/ratingplaceholderimage.md)
- [var placeholderVisibility: NSLevelIndicator.PlaceholderVisibility](nslevelindicator/placeholdervisibility-swift.property.md)
- [NSLevelIndicator.PlaceholderVisibility](nslevelindicator/placeholdervisibility-swift.enum.md)
### Controlling the Edit Behavior
- [var isEditable: Bool](nslevelindicator/iseditable.md)

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
- [Slider](slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator)*