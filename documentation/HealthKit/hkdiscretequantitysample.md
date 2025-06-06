# HKDiscreteQuantitySample

**Framework**: HealthKit  
**Kind**: class

A sample that represents a discrete quantity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKDiscreteQuantitySample
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)

#### Overview

A quantity sample contains one or more [`HKQuantity`](hkquantity.md) objects. Each quantity represents a single piece of data with a single numeric value and the value’s associated units. Use these samples to store data representing independent measurements, such as height, heart rate, or temperature.

The [`HKDiscreteQuantitySample`](hkdiscretequantitysample.md) class is a concrete subclass of the [`HKQuantitySample`](hkquantitysample.md) class. Discrete quantity samples are immutable; you set the sample’s properties when you create it, and they cannot change.

##### Extend Discrete Quantity Samples

Like many HealthKit classes, you should not subclass the [`HKDiscreteQuantitySample`](hkdiscretequantitysample.md) class. You may extend this class by adding metadata with custom keys to save related data used by your app.

For more information, see [`init(type:quantity:start:end:metadata:)`](hkquantitysample/init(type:quantity:start:end:metadata:).md).

## Topics

### Accessing Calculated Values
- [var averageQuantity: HKQuantity](hkdiscretequantitysample/averagequantity.md)
  The average of all quantities contained by the sample.
- [var maximumQuantity: HKQuantity](hkdiscretequantitysample/maximumquantity.md)
  The maximum quantity contained by the sample.
- [var minimumQuantity: HKQuantity](hkdiscretequantitysample/minimumquantity.md)
  The minimum value contained by the sample.
- [var mostRecentQuantity: HKQuantity](hkdiscretequantitysample/mostrecentquantity.md)
  The most recent quantity contained by the sample.
- [var mostRecentQuantityDateInterval: DateInterval](hkdiscretequantitysample/mostrecentquantitydateinterval.md)
  The date interval for the most recent quantity contained by the sample.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathMin: String](hkpredicatekeypathmin.md)
  The key path for the sample’s minimum quantity.
- [let HKPredicateKeyPathAverage: String](hkpredicatekeypathaverage.md)
  The key path for the sample’s average quantity.
- [let HKPredicateKeyPathMax: String](hkpredicatekeypathmax.md)
  The key path for the sample’s maximum quantity.
- [let HKPredicateKeyPathMostRecent: String](hkpredicatekeypathmostrecent.md)
  The key path for the sample’s most recent quantity.
- [let HKPredicateKeyPathMostRecentStartDate: String](hkpredicatekeypathmostrecentstartdate.md)
  The key path for the start date of the sample’s most recent quantity.
- [let HKPredicateKeyPathMostRecentEndDate: String](hkpredicatekeypathmostrecentenddate.md)
  The key path for the end date of the sample’s most recent quantity.
- [let HKPredicateKeyPathMostRecentDuration: String](hkpredicatekeypathmostrecentduration.md)
  A key path for the duration of the sample’s most recent quantity.

## Relationships

### Inherits From
- [HKQuantitySample](hkquantitysample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.
- [Metadata Keys](metadata-keys.md)
  Constants used to add metadata to objects stored in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdiscretequantitysample)*