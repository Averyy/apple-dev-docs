# calendarChooserDidFinish(_:)

**Framework**: EventKit UI  
**Kind**: method

Sent when a user selects one or more calendars.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func calendarChooserDidFinish(_ calendarChooser: EKCalendarChooser)
```

## Parameters

- `calendarChooser`: The calendar chooser that sent this message.

## See Also

- [func calendarChooserSelectionDidChange(EKCalendarChooser)](ekcalendarchooserdelegate/calendarchooserselectiondidchange(_:).md)
  Sent when a user changes the selection.
- [func calendarChooserDidCancel(EKCalendarChooser)](ekcalendarchooserdelegate/calendarchooserdidcancel(_:).md)
  Sent when the user cancels a calendar selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate/calendarchooserdidfinish(_:))*