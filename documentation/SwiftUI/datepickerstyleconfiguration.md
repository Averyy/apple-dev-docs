# DatePickerStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a `DatePicker`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DatePickerStyleConfiguration
```

## Topics

### Establishing the date range
- [var minimumDate: Date?](datepickerstyleconfiguration/minimumdate.md)
  The oldest selectable date.
- [var maximumDate: Date?](datepickerstyleconfiguration/maximumdate.md)
  The most recent selectable date.
### Labeling the date picker
- [let label: DatePickerStyleConfiguration.Label](datepickerstyleconfiguration/label-swift.property.md)
  A description of the `DatePicker`.
- [DatePickerStyleConfiguration.Label](datepickerstyleconfiguration/label-swift.struct.md)
  A type-erased label of a `DatePicker`.
- [var displayedComponents: DatePickerComponents](datepickerstyleconfiguration/displayedcomponents.md)
  The date components that the user is able to view and edit.
### Selecting the date
- [var selection: Date](datepickerstyleconfiguration/selection.md)
  The date value being displayed and selected.
- [var $selection: Binding<Date>](datepickerstyleconfiguration/$selection.md)

## See Also

- [func makeBody(configuration: Self.Configuration) -> Self.Body](datepickerstyle/makebody(configuration:).md)
  Returns the appearance and interaction content for a `DatePicker`.
- [DatePickerStyle.Configuration](datepickerstyle/configuration.md)
  A type alias for the properties of a `DatePicker`.
- [associatedtype Body : View](datepickerstyle/body.md)
  A view representing the appearance and interaction of a `DatePicker`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyleconfiguration)*