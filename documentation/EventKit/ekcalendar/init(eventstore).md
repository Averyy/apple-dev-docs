# init(eventStore:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a calendar belonging to a specified event store.

**Availability**:
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
init(eventStore: EKEventStore)
```

```objc
+ (EKCalendar *) calendarWithEventStore:(EKEventStore *) eventStore;
```

#### Return Value

The created calendar.

## Parameters

- `eventStore`: The event store to which the event belongs.

## See Also

### Creating Calendars
- [init(for: EKEntityType, eventStore: EKEventStore)](./init%28for,eventstore%29.md)
  Creates a new calendar that can contain the given entity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar/init(eventstore:))*