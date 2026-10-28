# calendarChooserSelectionDidChange(_:)

**Framework**: EventKit UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) calendarChooserSelectionDidChange:(EKCalendarChooser *) calendarChooser;
```

## Discussion

Use the [`selectedCalendars`](../ekcalendarchooser/selectedcalendars.md) property to get the current selection.

## Parameters

- `calendarChooser`: The calendar chooser that sent this message.

## See Also

### Selecting Calendars
- [func calendarChooserDidFinish(EKCalendarChooser)](./calendarchooserdidfinish%28_%29.md)
  Sent when a user selects one or more calendars.
- [func calendarChooserDidCancel(EKCalendarChooser)](./calendarchooserdidcancel%28_%29.md)
  Sent when the user cancels a calendar selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/calendarchooserselectiondidchange(_:))*