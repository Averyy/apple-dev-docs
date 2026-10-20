# predicateForEvaluatingTriggerOccurringBetweenDate(with:secondDateWith:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Type Method

Creates a predicate that evaluates whether the event occurred between the specified times.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func predicateForEvaluatingTriggerOccurringBetweenDate(with firstDateComponents: DateComponents, secondDateWith secondDateWithComponents: DateComponents) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForEvaluatingTriggerOccurringBetweenDateWithComponents:(NSDateComponents *) firstDateComponents secondDateWithComponents:(NSDateComponents *) secondDateWithComponents;
```

#### Return Value

A predicate object that represents a condition to evaluate before executing the scene.

## Parameters

- `firstDateComponents`: Date components that represent the first time boundary to compare to the execution time.
- `secondDateWithComponents`: Date components that represent the second time boundary to compare to the execution time.

## See Also

### Creating predicates
- [class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./predicateforevaluatingtriggeroccurring%28beforesignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTriggerOccurring(afterSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./predicateforevaluatingtriggeroccurring%28aftersignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred after a significant event.
- [class func predicate(forEvaluatingTriggerOccurringBetweenSignificantEvent: HMSignificantTimeEvent, secondSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./predicate%28forevaluatingtriggeroccurringbetweensignificantevent,secondsignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred between two significant events.
- [class func predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate](./predicateforevaluatingtrigger%28occurringbefore%29.md)
  Creates a predicate that evaluates whether the event occurred before the specified time.
- [class func predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate](./predicateforevaluatingtrigger%28occurringon%29.md)
  Creates a predicate that evaluates whether the event occurred at the specified time.
- [class func predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate](./predicateforevaluatingtrigger%28occurringafter%29.md)
  Creates a predicate that evaluates whether the event occurred at or after the specified time.
- [class func predicateForEvaluatingTrigger(HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate](./predicateforevaluatingtrigger%28_,relatedby,tovalue%29.md)
  Creates a predicate that evaluates whether a characteristic value relates to the specified value.
- [class func predicateForEvaluatingTrigger(withPresence: HMPresenceEvent) -> NSPredicate](./predicateforevaluatingtrigger%28withpresence%29.md)
  Creates a predicate that evaluates the current user presence against that specified in the presence event.
- [let HMCharacteristicKeyPath: String](../hmcharacteristickeypath.md)
  Specifies the key path for a characteristic in a predicate.
- [let HMCharacteristicValueKeyPath: String](../hmcharacteristicvaluekeypath.md)
  Specifies the key path for a characteristic value in a predicate.
- [let HMPresenceKeyPath: String](../hmpresencekeypath.md)
  Specifies the key path for a presence event in a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/predicateforevaluatingtriggeroccurringbetweendate(with:seconddatewith:))*