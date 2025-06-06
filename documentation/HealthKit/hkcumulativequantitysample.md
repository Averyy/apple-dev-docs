# HKCumulativeQuantitySample

**Framework**: HealthKit  
**Kind**: class

A sample that represents a cumulative quantity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKCumulativeQuantitySample
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)

#### Overview

A quantity sample contains one or more [`HKQuantity`](hkquantity.md) objects. Each quantity represents a single piece of data with a single numeric value and the value’s associated units. Use these samples to store data that accumulates over time, such as step count, active energy burned, or walking distance.

The [`HKCumulativeQuantitySample`](hkcumulativequantitysample.md) class is a concrete subclass of the [`HKQuantitySample`](hkquantitysample.md) class. Cumulative quantity samples are immutable; you set the sample’s properties when you create it, and they cannot change.

##### Extend Cumulative Quantity Samples

Like many HealthKit classes, you should not subclass the [`HKCumulativeQuantitySample`](hkcumulativequantitysample.md) class. You may extend this class by adding metadata with custom keys to save related data used by your app.

For more information, see [`init(type:quantity:start:end:metadata:)`](hkquantitysample/init(type:quantity:start:end:metadata:).md).

## Topics

### Accessing Calculated Data
- [var sumQuantity: HKQuantity](hkcumulativequantitysample/sumquantity.md)
  The sum of all the quantities contained by the sample.

## Relationships

### Inherits From
- [HKQuantitySample](hkquantitysample.md)
### Inherited By
- [HKCumulativeQuantitySeriesSample](hkcumulativequantityseriessample.md)
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

- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcumulativequantitysample)*