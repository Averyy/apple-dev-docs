# EKCalendarChooserDelegate

**Framework**: EventKit UI  
**Kind**: protocol  
**Role**: Protocol

Methods a calendar chooser’s delegate may use to receive notifications.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol EKCalendarChooserDelegate : NSObjectProtocol
```

```objc
@protocol EKCalendarChooserDelegate <NSObject>
```

## Topics

### Selecting Calendars
- [func calendarChooserDidFinish(EKCalendarChooser)](./ekcalendarchooserdelegate/calendarchooserdidfinish%28_%29.md)
  Sent when a user selects one or more calendars.
- [func calendarChooserSelectionDidChange(EKCalendarChooser)](./ekcalendarchooserdelegate/calendarchooserselectiondidchange%28_%29.md)
  Sent when a user changes the selection.
- [func calendarChooserDidCancel(EKCalendarChooser)](./ekcalendarchooserdelegate/calendarchooserdidcancel%28_%29.md)
  Sent when the user cancels a calendar selection.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing Calendar Selection
- [var delegate: (any EKCalendarChooserDelegate)?](./ekcalendarchooser/delegate.md)
  The calendar chooser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooserdelegate)*