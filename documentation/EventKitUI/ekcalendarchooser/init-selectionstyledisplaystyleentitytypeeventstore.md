# init(selectionStyle:displayStyle:entityType:eventStore:)

**Framework**: EventKit UI  
**Kind**: init

Initializes a newly created calendar chooser for a specific entity type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
init(selectionStyle style: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, entityType: EKEntityType, eventStore: EKEventStore)
```

#### Return Value

The initialized calendar chooser.

## Parameters

- `style`: Determines whether to allow selection of multiple calendars. Possible values are described in [`EKCalendarChooserSelectionStyle`](ekcalendarchooserselectionstyle.md).
- `displayStyle`: Determines which calendars to display. Possible values are described in [`EKCalendarChooserDisplayStyle`](ekcalendarchooserdisplaystyle.md).
- `entityType`: The entity type of the calendar. Possible values are [`EKEntityType.event`](https://developer.apple.com/documentation/EventKit/EKEntityType/event) and [`EKEntityType.reminder`](https://developer.apple.com/documentation/EventKit/EKEntityType/reminder).
- `eventStore`: The event store to which the calendars belong.

## See Also

- [init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, eventStore: EKEventStore)](ekcalendarchooser/init(selectionstyle:displaystyle:eventstore:).md)
  Initializes a newly created calendar chooser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/init(selectionstyle:displaystyle:entitytype:eventstore:))*