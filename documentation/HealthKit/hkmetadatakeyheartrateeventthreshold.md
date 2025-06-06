# HKMetadataKeyHeartRateEventThreshold

**Framework**: HealthKit  
**Kind**: var

A key that records the threshold of high or low heart rate events in beats per minute.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
let HKMetadataKeyHeartRateEventThreshold: String
```

#### Discussion

The value for this key contains an [`HKQuantity`](hkquantity.md) object with count/time units, described in [`HKUnit`](hkunit.md). This metadata key is used by [`highHeartRateEvent`](hkcategorytypeidentifier/highheartrateevent.md) and [`lowHeartRateEvent`](hkcategorytypeidentifier/lowheartrateevent.md) category samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyheartrateeventthreshold)*