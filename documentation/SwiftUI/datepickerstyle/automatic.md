# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default style for date pickers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var automatic: DefaultDatePickerStyle { get }
```

Available when `Self` is `DefaultDatePickerStyle`.

## See Also

### Getting built-in date picker styles
- [static var compact: CompactDatePickerStyle](./compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var field: FieldDatePickerStyle](./field.md)
  A date picker style that displays the components in an editable field.
- [static var graphical: GraphicalDatePickerStyle](./graphical.md)
  A date picker style that displays an interactive calendar or clock.
- [static var stepperField: StepperFieldDatePickerStyle](./stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [static var wheel: WheelDatePickerStyle](./wheel.md)
  A date picker style that displays each component as columns in a scrollable wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/automatic)*