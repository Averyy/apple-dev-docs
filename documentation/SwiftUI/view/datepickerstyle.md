# datePickerStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for date pickers within this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func datePickerStyle<S>(_ style: S) -> some View where S : DatePickerStyle
```

## See Also

- [struct DatePicker](datepicker.md)
  A control for selecting an absolute date.
- [struct MultiDatePicker](multidatepicker.md)
  A control for picking multiple dates.
- [var calendar: Calendar](environmentvalues/calendar.md)
  The current calendar that views should use when handling dates.
- [var timeZone: TimeZone](environmentvalues/timezone.md)
  The current time zone that views should use when handling dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/datepickerstyle(_:))*