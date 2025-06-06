# EKCalendarChooserDisplayStyle

**Framework**: EventKit UI  
**Kind**: enum

Indicates whether to display all calendars or writable calendars only.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum EKCalendarChooserDisplayStyle
```

## Topics

### Constants
- [EKCalendarChooserDisplayStyle.allCalendars](ekcalendarchooserdisplaystyle/allcalendars.md)
  Displays writable and read-only calendars.
- [EKCalendarChooserDisplayStyle.writableCalendarsOnly](ekcalendarchooserdisplaystyle/writablecalendarsonly.md)
  Displays writable calendars only.
### Initializers
- [init?(rawValue: Int)](ekcalendarchooserdisplaystyle/init(rawvalue:).md)

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
- [enum EKCalendarChooserSelectionStyle](ekcalendarchooserselectionstyle.md)
  Indicates whether users may select a single calendar, or multiple calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle)*