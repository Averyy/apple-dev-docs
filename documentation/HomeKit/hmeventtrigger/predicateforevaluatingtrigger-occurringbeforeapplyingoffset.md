# predicateForEvaluatingTrigger(occurringBefore:applyingOffset:)

**Framework**: HomeKit  
**Kind**: method

Creates a predicate that evaluates whether the event occurred before a significant event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func predicateForEvaluatingTrigger(occurringBefore significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate
```

#### Return Value

A predicate object that represents a condition to evaluate before executing the scene.

## Parameters

- `significantEvent`: The significant event to compare against. Valid values for this parameter are `HMSignificantEventSunrise` and `HMSignificantEventSunset`.
- `offset`: An offset from the time of the significant event. To specify an offset before a significant event, the properties of the [`NSDateComponents`](https://developer.apple.com/documentation/foundation/nsdatecomponents) object must be negative values. For example, to specify 30 minutes before sunset, set the [`minute`](https://developer.apple.com/documentation/foundation/nsdatecomponents/minute) property to `-30`.

## See Also

- [func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/addevent(_:completionhandler:).md)
  Adds a new event to the event trigger.
- [func removeEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](hmeventtrigger/removeevent(_:completionhandler:).md)
  Removes the specified event from the event trigger.
- [class func predicateForEvaluatingTrigger(occurringAfter: String, applyingOffset: DateComponents?) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:applyingoffset:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:applyingoffset:))*