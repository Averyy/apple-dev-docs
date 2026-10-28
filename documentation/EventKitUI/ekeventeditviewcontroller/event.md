# event

**Framework**: EventKit UI  
**Kind**: property  
**Role**: Instance Property

The event the user creates or edits using this view controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var event: EKEvent? { get set }
```

```objc
@property (nonatomic, retain, nullable) EKEvent * event;
```

## Discussion

If `nil`, creates and adds a new event to the default calendar’s event store. To avoid throwing an exception, ensure that the event is in the specified event store.

## See Also

### Creating and Saving Events
- [var eventStore: EKEventStore!](./eventstore.md)
  The event store used to save the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/event)*