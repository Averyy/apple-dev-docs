# NSStepperTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a stepper control for incrementing or decrementing a value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
class NSStepperTouchBarItem
```

## Topics

### Creating a stepper item
- [convenience init(identifier: NSTouchBarItem.Identifier, drawingHandler: (NSRect, Double) -> Void)](nssteppertouchbaritem/init(identifier:drawinghandler:).md)
  Creates a `NSStepperTouchBarItem` using the result of `drawingHandler` to display the stepper’s value as an image.
- [convenience init(identifier: NSTouchBarItem.Identifier, formatter: Formatter)](nssteppertouchbaritem/init(identifier:formatter:).md)
  Creates a `NSStepperTouchBarItem` with a `formatter` to display the stepper’s value as text.
### Handling stepper interaction
- [var target: AnyObject?](nssteppertouchbaritem/target.md)
  The target object that receives action messages from the stepper.
- [var action: Selector?](nssteppertouchbaritem/action.md)
  The action-message selector associated with the stepper.
### Managing the stepper’s value
- [var value: Double](nssteppertouchbaritem/value.md)
  The current value of the stepper.
- [var maxValue: Double](nssteppertouchbaritem/maxvalue.md)
  The stepper’s maximum value.
- [var minValue: Double](nssteppertouchbaritem/minvalue.md)
  The stepper’s minimum value.
- [var increment: Double](nssteppertouchbaritem/increment.md)
  The stepper’s increment value.
### Configuring bar customization
- [var customizationLabel: String!](nssteppertouchbaritem/customizationlabel.md)
  The localized string labeling this item during user customization.

## Relationships

### Inherits From
- [NSTouchBarItem](nstouchbaritem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSTouchBarItem](nstouchbaritem.md)
  A UI control shown in the Touch Bar on supported models of MacBook Pro.
- [class NSCandidateListTouchBarItem](nscandidatelisttouchbaritem.md)
  A bar item that, along with its delegate, provides a list of textual suggestions for the current text view.
- [class NSColorPickerTouchBarItem](nscolorpickertouchbaritem.md)
  A bar item that provides a system-defined color picker.
- [class NSCustomTouchBarItem](nscustomtouchbaritem.md)
  A bar item that contains a responder of your choice, such as a view, a button, or a scrubber.
- [class NSGroupTouchBarItem](nsgrouptouchbaritem.md)
  A bar item that provides a bar to contain other items.
- [class NSPopoverTouchBarItem](nspopovertouchbaritem.md)
  A bar item that provides a two-state control that can expand into its second state, showing the contents of a bar that it owns.
- [class NSSharingServicePickerTouchBarItem](nssharingservicepickertouchbaritem.md)
  A bar item that, along with its delegate, provides a list of objects eligible for sharing.
- [class NSSliderTouchBarItem](nsslidertouchbaritem.md)
  A bar item that provides a slider control for choosing a value in a range.
- [class NSUserInterfaceCompressionOptions](nsuserinterfacecompressionoptions.md)
  An object that specifies how user interface elements resize themselves when space is constrained.
- [class NSButtonTouchBarItem](nsbuttontouchbaritem.md)
  A bar item that provides a button.
- [class NSPickerTouchBarItem](nspickertouchbaritem.md)
  A bar item that provides a picker control with multiple options.
- [NSPickerTouchBarItem.ControlRepresentation](nspickertouchbaritem/controlrepresentation-swift.enum.md)
  Constants that specify display styles for picker bar items.
- [NSPickerTouchBarItem.SelectionMode](nspickertouchbaritem/selectionmode-swift.enum.md)
  Constants that specify selection modes for picker bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppertouchbaritem)*