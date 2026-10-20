# HMCharacteristicValueKeyPath

**Framework**: HomeKit  
**Kind**: var  
**Role**: Global Variable

Specifies the key path for a characteristic value in a predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicValueKeyPath: String
```

```c
extern NSString * const HMCharacteristicValueKeyPath;
```

## See Also

### Creating predicates
- [class func predicateForEvaluatingTriggerOccurring(beforeSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtriggeroccurring%28beforesignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred before a significant event.
- [class func predicateForEvaluatingTriggerOccurring(afterSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtriggeroccurring%28aftersignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred after a significant event.
- [class func predicate(forEvaluatingTriggerOccurringBetweenSignificantEvent: HMSignificantTimeEvent, secondSignificantEvent: HMSignificantTimeEvent) -> NSPredicate](./hmeventtrigger/predicate%28forevaluatingtriggeroccurringbetweensignificantevent,secondsignificantevent%29.md)
  Creates a predicate that evaluates whether the event occurred between two significant events.
- [class func predicateForEvaluatingTrigger(occurringBefore: DateComponents) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtrigger%28occurringbefore%29.md)
  Creates a predicate that evaluates whether the event occurred before the specified time.
- [class func predicateForEvaluatingTrigger(occurringOn: DateComponents) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtrigger%28occurringon%29.md)
  Creates a predicate that evaluates whether the event occurred at the specified time.
- [class func predicateForEvaluatingTrigger(occurringAfter: DateComponents) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtrigger%28occurringafter%29.md)
  Creates a predicate that evaluates whether the event occurred at or after the specified time.
- [class func predicateForEvaluatingTriggerOccurringBetweenDate(with: DateComponents, secondDateWith: DateComponents) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtriggeroccurringbetweendate%28with,seconddatewith%29.md)
  Creates a predicate that evaluates whether the event occurred between the specified times.
- [class func predicateForEvaluatingTrigger(HMCharacteristic, relatedBy: NSComparisonPredicate.Operator, toValue: Any) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtrigger%28_,relatedby,tovalue%29.md)
  Creates a predicate that evaluates whether a characteristic value relates to the specified value.
- [class func predicateForEvaluatingTrigger(withPresence: HMPresenceEvent) -> NSPredicate](./hmeventtrigger/predicateforevaluatingtrigger%28withpresence%29.md)
  Creates a predicate that evaluates the current user presence against that specified in the presence event.
- [let HMCharacteristicKeyPath: String](./hmcharacteristickeypath.md)
  Specifies the key path for a characteristic in a predicate.
- [let HMPresenceKeyPath: String](./hmpresencekeypath.md)
  Specifies the key path for a presence event in a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluekeypath)*