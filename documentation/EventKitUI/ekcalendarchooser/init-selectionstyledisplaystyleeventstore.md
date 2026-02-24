# init(selectionStyle:displayStyle:eventStore:)

**Framework**: EventKit UI  
**Kind**: init

Initializes a newly created calendar chooser.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, eventStore: EKEventStore)
```

#### Return Value

The initialized calendar chooser.

## Parameters

- `selectionStyle`: Determines whether to allow selection of multiple calendars. Possible values are described in [`EKCalendarChooserSelectionStyle`](ekcalendarchooserselectionstyle.md).
- `displayStyle`: Determines which calendars to display. Possible values are described in [`EKCalendarChooserDisplayStyle`](ekcalendarchooserdisplaystyle.md).
- `eventStore`: The event store to which the calendars belong.

## See Also

- [init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, entityType: EKEntityType, eventStore: EKEventStore)](ekcalendarchooser/init(selectionstyle:displaystyle:entitytype:eventstore:).md)
  Initializes a newly created calendar chooser for a specific entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser/init(selectionstyle:displaystyle:eventstore:))*