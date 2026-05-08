# field

**Framework**: SwiftUI  
**Kind**: property

A date picker style that displays the components in an editable field.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static var field: FieldDatePickerStyle { get }
```

#### Discussion

You can use this style when space is constrained and users expect to make specific date and time selections. However, you should generally use [`stepperField`](datepickerstyle/stepperfield.md) instead of this style, unless your your app requires hiding the stepper.

## See Also

- [static var automatic: DefaultDatePickerStyle](datepickerstyle/automatic.md)
  The default style for date pickers.
- [static var compact: CompactDatePickerStyle](datepickerstyle/compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var graphical: GraphicalDatePickerStyle](datepickerstyle/graphical.md)
  A date picker style that displays an interactive calendar or clock.
- [static var stepperField: StepperFieldDatePickerStyle](datepickerstyle/stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [static var wheel: WheelDatePickerStyle](datepickerstyle/wheel.md)
  A date picker style that displays each component as columns in a scrollable wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/field)*