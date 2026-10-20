# EKCalendarChooserDisplayStyle

**Framework**: EventKit UI  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum EKCalendarChooserDisplayStyle : NSInteger;
```

## Topics

### Constants
- [EKCalendarChooserDisplayStyle.allCalendars](./ekcalendarchooserdisplaystyle/allcalendars.md)
  Displays writable and read-only calendars.
- [EKCalendarChooserDisplayStyle.writableCalendarsOnly](./ekcalendarchooserdisplaystyle/writablecalendarsonly.md)
  Displays writable calendars only.
### Initializers
- [init?(rawValue: Int)](./ekcalendarchooserdisplaystyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting a Calendar Type
- [var selectedCalendars: Set<EKCalendar>](./ekcalendarchooser/selectedcalendars.md)
  The calendars selected by the user.
- [var selectionStyle: EKCalendarChooserSelectionStyle](./ekcalendarchooser/selectionstyle.md)
  Determines whether to allow selection of multiple calendars.
- [enum EKCalendarChooserSelectionStyle](./ekcalendarchooserselectionstyle.md)
  Indicates whether users may select a single calendar, or multiple calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdisplaystyle)*