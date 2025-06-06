# graphical

**Framework**: SwiftUI  
**Kind**: property

A date picker style that displays an interactive calendar or clock.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var graphical: GraphicalDatePickerStyle { get }
```

#### Discussion

This style is useful when you want to allow browsing through days in a calendar, or when the look of a clock face is appropriate.

## See Also

- [static var automatic: DefaultDatePickerStyle](datepickerstyle/automatic.md)
  The default style for date pickers.
- [static var compact: CompactDatePickerStyle](datepickerstyle/compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var field: FieldDatePickerStyle](datepickerstyle/field.md)
  A date picker style that displays the components in an editable field.
- [static var stepperField: StepperFieldDatePickerStyle](datepickerstyle/stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [static var wheel: WheelDatePickerStyle](datepickerstyle/wheel.md)
  A date picker style that displays each component as columns in a scrollable wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/graphical)*