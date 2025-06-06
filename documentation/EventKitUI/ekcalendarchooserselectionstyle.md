# EKCalendarChooserSelectionStyle

**Framework**: EventKit UI  
**Kind**: enum

Indicates whether users may select a single calendar, or multiple calendars.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum EKCalendarChooserSelectionStyle
```

## Topics

### Constants
- [EKCalendarChooserSelectionStyle.single](ekcalendarchooserselectionstyle/single.md)
  A style that limits users to selecting a single calendar.
- [EKCalendarChooserSelectionStyle.multiple](ekcalendarchooserselectionstyle/multiple.md)
  A style that lets users select multiple calendars.
### Initializers
- [init?(rawValue: Int)](ekcalendarchooserselectionstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selectedCalendars: Set<EKCalendar>](ekcalendarchooser/selectedcalendars.md)
  The calendars selected by the user.
- [var selectionStyle: EKCalendarChooserSelectionStyle](ekcalendarchooser/selectionstyle.md)
  Determines whether to allow selection of multiple calendars.
- [enum EKCalendarChooserDisplayStyle](ekcalendarchooserdisplaystyle.md)
  Indicates whether to display all calendars or writable calendars only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserselectionstyle)*