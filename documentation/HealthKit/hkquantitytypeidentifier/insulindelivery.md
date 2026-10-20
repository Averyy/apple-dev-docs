# insulinDelivery

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample that measures the amount of insulin delivered.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let insulinDelivery: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierInsulinDelivery;
```

#### Discussion

These samples use international units (IU) (described in [`HKUnit`](../hkunit.md)) and measure cumulative values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## Topics

### Metadata Keys
- [let HKMetadataKeyInsulinDeliveryReason: String](../hkmetadatakeyinsulindeliveryreason.md)
  The medical reason for administering insulin.

## See Also

### Related Documentation
- [struct HKQuantityTypeIdentifier](../hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](../hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKQuantity](../hkquantity.md)
  An object that stores a value for a given unit.
### Lab and test results
- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](./bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let bloodGlucose: HKQuantityTypeIdentifier](./bloodglucose.md)
  A quantity sample type that measures the user’s blood glucose level.
- [static let electrodermalActivity: HKQuantityTypeIdentifier](./electrodermalactivity.md)
  A quantity sample type that measures electrodermal activity.
- [static let forcedExpiratoryVolume1: HKQuantityTypeIdentifier](./forcedexpiratoryvolume1.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs during the first second of a forced exhalation.
- [static let forcedVitalCapacity: HKQuantityTypeIdentifier](./forcedvitalcapacity.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs after taking the deepest breath possible.
- [static let inhalerUsage: HKQuantityTypeIdentifier](./inhalerusage.md)
  A quantity sample type that measures the number of puffs the user takes from their inhaler.
- [static let numberOfTimesFallen: HKQuantityTypeIdentifier](./numberoftimesfallen.md)
  A quantity sample type that measures the number of times the user fell.
- [static let peakExpiratoryFlowRate: HKQuantityTypeIdentifier](./peakexpiratoryflowrate.md)
  A quantity sample type that measures the user’s maximum flow rate generated during a forceful exhalation.
- [static let peripheralPerfusionIndex: HKQuantityTypeIdentifier](./peripheralperfusionindex.md)
  A quantity sample type that measures the user’s peripheral perfusion index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/insulindelivery)*