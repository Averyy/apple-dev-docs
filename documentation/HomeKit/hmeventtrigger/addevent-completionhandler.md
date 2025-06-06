# addEvent(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a new event to the event trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addEvent(_ event: HMEvent) async throws
```

## Parameters

- `event`: An event to add to the event trigger.
- `completion`: The block takes the following parameter:

## See Also

- [func removeEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/removeevent(_:completionhandler:).md)
  Removes the specified event from the event trigger.
- [class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/addevent(_:completionhandler:))*