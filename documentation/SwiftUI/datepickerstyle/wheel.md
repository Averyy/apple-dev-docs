# wheel

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A date picker style that displays each component as columns in a scrollable wheel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var wheel: WheelDatePickerStyle { get }
```

Available when `Self` is `WheelDatePickerStyle`.

## See Also

### Getting built-in date picker styles
- [static var automatic: DefaultDatePickerStyle](./automatic.md)
  The default style for date pickers.
- [static var compact: CompactDatePickerStyle](./compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var field: FieldDatePickerStyle](./field.md)
  A date picker style that displays the components in an editable field.
- [static var graphical: GraphicalDatePickerStyle](./graphical.md)
  A date picker style that displays an interactive calendar or clock.
- [static var stepperField: StepperFieldDatePickerStyle](./stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/wheel)*