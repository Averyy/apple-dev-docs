# DatePickerComponents

**Framework**: SwiftUI  
**Kind**: struct

The date and time components that a date picker shows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DatePickerComponents
```

#### Overview

Pass a value of this type as the `displayedComponents` argument of a [`DatePicker`](datepicker.md) initializer to choose which parts of a date someone can edit. Combine options to show more than one group.

```swift
DatePicker(
    "Departure",
    selection: $departure,
    displayedComponents: [.hourAndMinute, .date]
)
```

A picker shows `[.hourAndMinute, .date]` unless you choose otherwise. Each option respects the current locale, so [`date`](datepickercomponents/date.md) orders the day, month, and year the way the person’s region expects.

## Topics

### Getting date picker components
- [static let date: DatePickerComponents](datepickercomponents/date.md)
  Displays day, month, and year based on the locale
- [static let hourAndMinute: DatePickerComponents](datepickercomponents/hourandminute.md)
  Displays hour and minute components based on the locale
- [static let hourMinuteAndSecond: DatePickerComponents](datepickercomponents/hourminuteandsecond.md)
  Displays hour, minute and second components based on the locale

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [DatePicker.Components](datepicker/components.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickercomponents)*