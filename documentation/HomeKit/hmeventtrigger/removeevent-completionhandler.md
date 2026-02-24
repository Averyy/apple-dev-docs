# removeEvent(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes the specified event from the event trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func removeEvent(_ event: HMEvent) async throws
```

## Parameters

- `event`: The event to remove from the event trigger.
- `completion`: A block that executes after processing the request. The block takes the following parameter: - **error**: If the request was successful, the value of `error` is `nil`; otherwise, the value provides more information about the request status.

## See Also

- [func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/addevent(_:completionhandler:).md)
  Adds a new event to the event trigger.
- [class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/removeevent(_:completionhandler:))*