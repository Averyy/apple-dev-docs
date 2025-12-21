# DatePickerStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that specifies the appearance and interaction of all date pickers within a view hierarchy.

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
@preconcurrency protocol DatePickerStyle
```

#### Overview

To configure the current date picker style for a view hierarchy, use the [`datePickerStyle(_:)`](view/datepickerstyle(_:).md) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in date picker styles
- [static var automatic: DefaultDatePickerStyle](datepickerstyle/automatic.md)
  The default style for date pickers.
- [static var compact: CompactDatePickerStyle](datepickerstyle/compact.md)
  A date picker style that displays the components in a compact, textual format.
- [static var field: FieldDatePickerStyle](datepickerstyle/field.md)
  A date picker style that displays the components in an editable field.
- [static var graphical: GraphicalDatePickerStyle](datepickerstyle/graphical.md)
  A date picker style that displays an interactive calendar or clock.
- [static var stepperField: StepperFieldDatePickerStyle](datepickerstyle/stepperfield.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [static var wheel: WheelDatePickerStyle](datepickerstyle/wheel.md)
  A date picker style that displays each component as columns in a scrollable wheel.
### Creating custom date picker styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](datepickerstyle/makebody(configuration:).md)
  Returns the appearance and interaction content for a `DatePicker`.
- [struct DatePickerStyleConfiguration](datepickerstyleconfiguration.md)
  The properties of a `DatePicker`.
- [DatePickerStyle.Configuration](datepickerstyle/configuration.md)
  A type alias for the properties of a `DatePicker`.
- [associatedtype Body : View](datepickerstyle/body.md)
  A view representing the appearance and interaction of a `DatePicker`.
### Supporting types
- [struct DefaultDatePickerStyle](defaultdatepickerstyle.md)
  The default style for date pickers.
- [struct CompactDatePickerStyle](compactdatepickerstyle.md)
  A date picker style that displays the components in a compact, textual format.
- [struct FieldDatePickerStyle](fielddatepickerstyle.md)
  A date picker style that displays the components in an editable field.
- [struct GraphicalDatePickerStyle](graphicaldatepickerstyle.md)
  A date picker style that displays an interactive calendar or clock.
- [struct StepperFieldDatePickerStyle](stepperfielddatepickerstyle.md)
  A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [struct WheelDatePickerStyle](wheeldatepickerstyle.md)
  A date picker style that displays each component as columns in a scrollable wheel.

## Relationships

### Conforming Types
- [CompactDatePickerStyle](compactdatepickerstyle.md)
- [DefaultDatePickerStyle](defaultdatepickerstyle.md)
- [FieldDatePickerStyle](fielddatepickerstyle.md)
- [GraphicalDatePickerStyle](graphicaldatepickerstyle.md)
- [StepperFieldDatePickerStyle](stepperfielddatepickerstyle.md)
- [WheelDatePickerStyle](wheeldatepickerstyle.md)

## See Also

- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [protocol PickerStyle](pickerstyle.md)
  A type that specifies the appearance and interaction of all pickers within a view hierarchy.
- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle)*