# init(name:events:end:recurrences:predicate:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a new event trigger with the specified name, events, end events, recurrences, and predicate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(name: String, events: [HMEvent], end endEvents: [HMEvent]?, recurrences: [DateComponents]?, predicate: NSPredicate?)
```

```objc
- (instancetype) initWithName:(NSString *) name events:(NSArray<HMEvent *> *) events endEvents:(NSArray<HMEvent *> *) endEvents recurrences:(NSArray<NSDateComponents *> *) recurrences predicate:(NSPredicate *) predicate;
```

## Return Value

An initialized event trigger.

## Parameters

- `name`: The name of the event trigger.
- `events`: An array of events that can activate the evaluation of the event trigger. The trigger is evaluated if any one of the events is true.
- `endEvents`: An array of events that can trigger the end of the scene that this event trigger represents.
- `recurrences`: Specifies the days of the week to evaluate the trigger. All properties other than [`weekday`](../../Foundation/datecomponents/weekday.md) on [`DateComponents`](../../Foundation/datecomponents.md) are ignored.
- `predicate`: The predicate to test and activate after evaluating the event trigger. Once activated, the event’s scenes execute. If a value isn’t specified the event trigger executes the scene if any of the events activate.

## See Also

### Creating an event trigger
- [init(name: String, events: [HMEvent], predicate: NSPredicate?)](./init%28name,events,predicate%29.md)
  Creates a new event trigger with the specified name, events, and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/init(name:events:end:recurrences:predicate:))*