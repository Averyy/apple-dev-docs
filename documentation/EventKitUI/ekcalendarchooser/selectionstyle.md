# selectionStyle

**Framework**: EventKit UI  
**Kind**: property  
**Role**: Instance Property

Determines whether to allow selection of multiple calendars.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var selectionStyle: EKCalendarChooserSelectionStyle { get }
```

```objc
@property (nonatomic, readonly) EKCalendarChooserSelectionStyle selectionStyle;
```

#### Discussion

Possible values are described in [`EKCalendarChooserSelectionStyle`](../ekcalendarchooserselectionstyle.md).

## See Also

### Selecting a Calendar Type
- [var selectedCalendars: Set<EKCalendar>](./selectedcalendars.md)
  The calendars selected by the user.
- [enum EKCalendarChooserSelectionStyle](../ekcalendarchooserselectionstyle.md)
  Indicates whether users may select a single calendar, or multiple calendars.
- [enum EKCalendarChooserDisplayStyle](../ekcalendarchooserdisplaystyle.md)
  Indicates whether to display all calendars or writable calendars only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/selectionstyle)*