# calendarChooserSelectionDidChange(_:)

**Framework**: EventKit UI  
**Kind**: method

Sent when a user changes the selection.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func calendarChooserSelectionDidChange(_ calendarChooser: EKCalendarChooser)
```

#### Discussion

Use the [`selectedCalendars`](ekcalendarchooser/selectedcalendars.md) property to get the current selection.

## Parameters

- `calendarChooser`: The calendar chooser that sent this message.

## See Also

- [func calendarChooserDidFinish(EKCalendarChooser)](ekcalendarchooserdelegate/calendarchooserdidfinish(_:).md)
  Sent when a user selects one or more calendars.
- [func calendarChooserDidCancel(EKCalendarChooser)](ekcalendarchooserdelegate/calendarchooserdidcancel(_:).md)
  Sent when the user cancels a calendar selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/calendarchooserselectiondidchange(_:))*