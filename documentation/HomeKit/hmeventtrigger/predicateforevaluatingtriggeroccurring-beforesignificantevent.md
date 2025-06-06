# predicateForEvaluatingTriggerOccurring(beforeSignificantEvent:)

**Framework**: HomeKit  
**Kind**: method

Creates a predicate that evaluates whether the event occurred before a significant event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent significantEvent: HMSignificantTimeEvent) -> NSPredicate
```

#### Return Value

A predicate object that represents a condition to evaluate before executing the scene.

## Parameters

- `significantEvent`: The significant event to compare against.

## See Also

- [class func predicateForEvaluatingTriggerOccurring(afterSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurring(aftersignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred after a significant event.
- [class func predicate(forEvaluatingTriggerOccurringBetweenSignificantEvent: HMSignificantTimeEvent, secondSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicate(forevaluatingtriggeroccurringbetweensignificantevent:secondsignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred between two significant events.
- [class func predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringbefore:).md)
  Creates a predicate that evaluates whether the event occurred before the specified time.
- [class func predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringon:).md)
  Creates a predicate that evaluates whether the event occurred at the specified time.
- [class func predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(occurringafter:).md)
  Creates a predicate that evaluates whether the event occurred at or after the specified time.
- [class func predicateForEvaluatingTriggerOccurringBetweenDate(with: DateComponents, secondDateWith: DateComponents) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurringbetweendate(with:seconddatewith:).md)
  Creates a predicate that evaluates whether the event occurred between the specified times.
- [class func predicateForEvaluatingTrigger(HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(_:relatedby:tovalue:).md)
  Creates a predicate that evaluates whether a characteristic value relates to the specified value.
- [class func predicateForEvaluatingTrigger(withPresence: HMPresenceEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtrigger(withpresence:).md)
  Creates a predicate that evaluates the current user presence against that specified in the presence event.
- [let HMCharacteristicKeyPath: String](hmcharacteristickeypath.md)
  Specifies the key path for a characteristic in a predicate.
- [let HMCharacteristicValueKeyPath: String](hmcharacteristicvaluekeypath.md)
  Specifies the key path for a characteristic value in a predicate.
- [let HMPresenceKeyPath: String](hmpresencekeypath.md)
  Specifies the key path for a presence event in a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/predicateforevaluatingtriggeroccurring(beforesignificantevent:))*