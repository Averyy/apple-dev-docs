# waterTemperature

**Framework**: HealthKit  
**Kind**: property

A quantity sample that records the water temperature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let waterTemperature: HKQuantityTypeIdentifier
```

#### Discussion

Apple Watch Ultra automatically records these samples during dive sessions and swimming workouts.

Water temperature samples use temperature units (see [`HKUnit`](hkunit.md)) and measure discrete values (see [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

## See Also

- [static let underwaterDepth: HKQuantityTypeIdentifier](hkquantitytypeidentifier/underwaterdepth.md)
  A quantity sample that records a person’s depth underwater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/watertemperature)*