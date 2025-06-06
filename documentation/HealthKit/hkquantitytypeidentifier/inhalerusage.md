# inhalerUsage

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the number of puffs the user takes from their inhaler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let inhalerUsage: HKQuantityTypeIdentifier
```

#### Discussion

These samples use count units (described in [`HKUnit`](hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

## See Also

- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let bloodGlucose: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodglucose.md)
  A quantity sample type that measures the user’s blood glucose level.
- [static let electrodermalActivity: HKQuantityTypeIdentifier](hkquantitytypeidentifier/electrodermalactivity.md)
  A quantity sample type that measures electrodermal activity.
- [static let forcedExpiratoryVolume1: HKQuantityTypeIdentifier](hkquantitytypeidentifier/forcedexpiratoryvolume1.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs during the first second of a forced exhalation.
- [static let forcedVitalCapacity: HKQuantityTypeIdentifier](hkquantitytypeidentifier/forcedvitalcapacity.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs after taking the deepest breath possible.
- [static let insulinDelivery: HKQuantityTypeIdentifier](hkquantitytypeidentifier/insulindelivery.md)
  A quantity sample that measures the amount of insulin delivered.
- [static let numberOfTimesFallen: HKQuantityTypeIdentifier](hkquantitytypeidentifier/numberoftimesfallen.md)
  A quantity sample type that measures the number of times the user fell.
- [static let peakExpiratoryFlowRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/peakexpiratoryflowrate.md)
  A quantity sample type that measures the user’s maximum flow rate generated during a forceful exhalation.
- [static let peripheralPerfusionIndex: HKQuantityTypeIdentifier](hkquantitytypeidentifier/peripheralperfusionindex.md)
  A quantity sample type that measures the user’s peripheral perfusion index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/inhalerusage)*