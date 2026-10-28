# predicateForEvaluatingTrigger(occurringAfter:applyingOffset:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Type Method

Creates a predicate that evaluates whether the event occurred before a significant event.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`predicateForEvaluatingTriggerOccurring(afterSignificantEvent:)`](./predicateforevaluatingtriggeroccurring%28aftersignificantevent%29.md) instead.

## Declaration

```swift
class func predicateForEvaluatingTrigger(occurringAfter significantEvent: String, applyingOffset offset: DateComponents?) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForEvaluatingTriggerOccurringAfterSignificantEvent:(NSString *) significantEvent applyingOffset:(NSDateComponents *) offset;
```

## Return Value

A predicate object that represents a condition to evaluate before executing the scene.

## Parameters

- `significantEvent`: The significant event to compare against. Valid values for this parameter are `HMSignificantEventSunrise` and `HMSignificantEventSunset`.
- `offset`: An offset from the time of the significant event. To specify an offset after a significant event, the properties of the [`NSDateComponents`](../../Foundation/nsdatecomponents.md) object must be positive values. For example, to specify 30 minutes after sunset, set the [`minute`](../../Foundation/nsdatecomponents/minute.md) property to `30`.

## See Also

### Deprecated symbols
- [func addEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](./addevent%28_,completionhandler%29.md)
  Adds a new event to the event trigger.
- [func removeEvent(HMEvent, completionHandler: ((any Error)?) -> Void)](./removeevent%28_,completionhandler%29.md)
  Removes the specified event from the event trigger.
- [class func predicateForEvaluatingTrigger(occurringBefore: String, applyingOffset: DateComponents?) -> NSPredicate](./predicateforevaluatingtrigger%28occurringbefore,applyingoffset%29.md)
  Creates a predicate that evaluates whether the event occurred before a significant event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/predicateforevaluatingtrigger(occurringafter:applyingoffset:))*