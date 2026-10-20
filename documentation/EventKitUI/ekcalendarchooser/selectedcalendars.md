# selectedCalendars

**Framework**: EventKit UI  
**Kind**: property  
**Role**: Instance Property

The calendars selected by the user.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var selectedCalendars: Set<EKCalendar> { get set }
```

```objc
@property (nonatomic, copy) NSSet<EKCalendar *> * selectedCalendars;
```

## See Also

### Selecting a Calendar Type
- [var selectionStyle: EKCalendarChooserSelectionStyle](./selectionstyle.md)
  Determines whether to allow selection of multiple calendars.
- [enum EKCalendarChooserSelectionStyle](../ekcalendarchooserselectionstyle.md)
  Indicates whether users may select a single calendar, or multiple calendars.
- [enum EKCalendarChooserDisplayStyle](../ekcalendarchooserdisplaystyle.md)
  Indicates whether to display all calendars or writable calendars only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/selectedcalendars)*