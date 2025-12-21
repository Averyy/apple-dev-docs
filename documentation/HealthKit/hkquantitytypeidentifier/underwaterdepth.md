# underwaterDepth

**Framework**: HealthKit  
**Kind**: property

A quantity sample that records a person’s depth underwater.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let underwaterDepth: HKQuantityTypeIdentifier
```

#### Discussion

Apple Watch Ultra automatically records these samples during dive sessions.

Underwater depth samples use length units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). Sample data may be condensed and/or coalesced by HealthKit. For more information, see [`Accessing condensed workout samples`](accessing-condensed-workout-samples.md).

## See Also

- [static let waterTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/watertemperature.md)
  A quantity sample that records the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/underwaterdepth)*