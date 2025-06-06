# init(for:eventStore:)

**Framework**: EventKit  
**Kind**: init

Creates a new calendar that can contain the given entity type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(for entityType: EKEntityType, eventStore: EKEventStore)
```

#### Return Value

The created calendar.

#### Discussion

You can only create calendars that accept either reminders or events. Some servers might allow mixing the two, although it is not common.

## Parameters

- `entityType`: The entity type that this calendar may support.
- `eventStore`: The event store in which to create this calendar.

## See Also

- [init(eventStore: EKEventStore)](ekcalendar/init(eventstore:).md)
  Creates and returns a calendar belonging to a specified event store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/init(for:eventstore:))*