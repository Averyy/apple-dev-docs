# timeInDaylight

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures amount of time the user spent in daylight.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let timeInDaylight: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierTimeInDaylight;
```

## Discussion

These samples use time units (described in [`HKUnit`](../hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### UV exposure
- [static let uvExposure: HKQuantityTypeIdentifier](./uvexposure.md)
  A quantity sample type that measures the user’s exposure to UV radiation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/timeindaylight)*