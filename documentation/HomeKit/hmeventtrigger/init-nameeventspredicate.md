# init(name:events:predicate:)

**Framework**: HomeKit  
**Kind**: init

Creates a new event trigger with the specified name, events, and predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String, events: [HMEvent], predicate: NSPredicate?)
```

## Parameters

- `name`: The name of the event trigger.
- `events`: An array of events that can activate the evaluation of the event trigger. The trigger is evaluated if any one of the events is true.
- `predicate`: The predicate to test and activate after evaluating the event trigger. Once activated, the event’s scenes execute. If a value isn’t specified the event trigger executes the scene if any of the events activate.

## See Also

- [init(name: String, events: [HMEvent], end: [HMEvent]?, recurrences: [DateComponents]?, predicate: NSPredicate?)](hmeventtrigger/init(name:events:end:recurrences:predicate:).md)
  Creates a new event trigger with the specified name, events, end events, recurrences, and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/init(name:events:predicate:))*