# HKQuantitySample

**Framework**: HealthKit  
**Kind**: class

A sample that represents a quantity, including the value and the units.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKQuantitySample
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

A quantity sample contains one or more [`HKQuantity`](hkquantity.md) objects. Each quantity represents a single piece of data with a single numeric value and the value’s associated units. For example, you can use quantity samples to record the user’s height, the user’s current heart rate, or the number of calories in a hamburger. HealthKit provides a wide range of quantity types, letting you track many different health and fitness features.

The [`HKQuantitySample`](hkquantitysample.md) class is a subclass of the [`HKSample`](hksample.md) class. Quantity samples are immutable; you set the sample’s properties when you create it, and they cannot change.

In iOS 13 and later and watchOS 6 and later, [`HKQuantitySample`](hkquantitysample.md) is an abstract superclass for the [`HKCumulativeQuantitySample`](hkcumulativequantitysample.md) and [`HKDiscreteQuantitySample`](hkdiscretequantitysample.md) concrete subclasses. The system automatically selects the correct subclass based on the [`HKQuantityType`](hkquantitytype.md) object used to create the sample.

##### Extend Quantity Samples

Like many HealthKit classes, you should not subclass the [`HKQuantitySample`](hkquantitysample.md) class. You may extend this class by adding metadata with custom keys to save related data used by your app.

For more information, see [`init(type:quantity:start:end:metadata:)`](hkquantitysample/init(type:quantity:start:end:metadata:).md).

## Topics

### Creating Quantity Samples
- [convenience init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date)](hkquantitysample/init(type:quantity:start:end:).md)
  Returns a sample containing a numeric measurement.
- [convenience init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, metadata: [String : Any]?)](hkquantitysample/init(type:quantity:start:end:metadata:).md)
  Returns a sample containing a numeric measurement with the provided metadata.
- [convenience init(type: HKQuantityType, quantity: HKQuantity, start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkquantitysample/init(type:quantity:start:end:device:metadata:).md)
  Returns a sample containing a numeric measurement with the provided device and metadata.
### Getting Property Data
- [var quantity: HKQuantity](hkquantitysample/quantity.md)
  The quantity for this sample.
- [var count: Int](hkquantitysample/count.md)
  The number of quantities contained in this sample.
- [var quantityType: HKQuantityType](hkquantitysample/quantitytype.md)
  The quantity type for this sample.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathQuantity: String](hkpredicatekeypathquantity.md)
  The key path for accessing the sample’s quantity.
- [let HKPredicateKeyPathCount: String](hkpredicatekeypathcount.md)
  A key path for the sample’s count.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Inherited By
- [HKCumulativeQuantitySample](hkcumulativequantitysample.md)
- [HKDiscreteQuantitySample](hkdiscretequantitysample.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.
- [Metadata Keys](metadata-keys.md)
  Constants used to add metadata to objects stored in HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample)*