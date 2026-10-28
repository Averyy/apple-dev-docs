# field

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A date picker style that displays the components in an editable field.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var field: FieldDatePickerStyle { get }
```

Available when `Self` is `FieldDatePickerStyle`.

## Discussion

You can use this style when space is constrained and users expect to make specific date and time selections. However, you should generally use [`stepperField`](./stepperfield.md) instead of this style, unless your your app requires hiding the stepper.

## See Also

### Getting built-in date picker styles
- [static var automatic: DefaultDatePickerStyle](./automatic.md)
  The default style for date pickers.
- [static var compact: CompactDatePickerStyle](./compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var graphical: GraphicalDatePickerStyle](./graphical.md)
  A date picker style that displays an interactive calendar or clock.
- [static var stepperField: StepperFieldDatePickerStyle](./stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [static var wheel: WheelDatePickerStyle](./wheel.md)
  A date picker style that displays each component as columns in a scrollable wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/field)*