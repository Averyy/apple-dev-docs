# HMCharacteristicKeyPath

**Framework**: HomeKit  
**Kind**: var

Specifies the key path for a characteristic in a predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicKeyPath: String
```

## See Also

- [class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](hmeventtrigger/predicateforevaluatingtriggeroccurring(beforesignificantevent:).md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
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
- [let HMCharacteristicValueKeyPath: String](hmcharacteristicvaluekeypath.md)
  Specifies the key path for a characteristic value in a predicate.
- [let HMPresenceKeyPath: String](hmpresencekeypath.md)
  Specifies the key path for a presence event in a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristickeypath)*