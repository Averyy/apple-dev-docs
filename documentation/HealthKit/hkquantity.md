# HKQuantity

**Framework**: HealthKit  
**Kind**: class

An object that stores a value for a given unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKQuantity
```

## Mentions

- [Defining and converting units and quantities](defining-and-converting-units-and-quantities.md)
- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

HealthKit uses quantity objects to store numerical data. When you create a quantity, you provide both the quantity’s value and unit.

Quantities are immutable objects: Their values are set when the object is first created and cannot change.

##### Converting Units

You can request the value from a quantity object in any compatible units. For example,  if you create a length quantity in feet, you can then request the length in meters. The quantity object automatically converts its value to the requested units.

##### Using Quantities

Like many HealthKit classes, the [`HKQuantity`](hkquantity.md) class is not extendible and should not be subclassed. To help promote sharing data between apps, [`HKQuantity`](hkquantity.md) objects use only the units defined by the [`HKUnit`](hkunit.md) class.

## Topics

### Creating Quantities
- [convenience init(unit: HKUnit, doubleValue: Double)](hkquantity/init(unit:doublevalue:).md)
  Instantiates and returns a new quantity object.
### Working With Units
- [func `is`(compatibleWith: HKUnit) -> Bool](hkquantity/is(compatiblewith:).md)
  Returns a boolean value indicating whether the quantity is compatible with the provided unit.
- [func doubleValue(for: HKUnit) -> Double](hkquantity/doublevalue(for:).md)
  Returns the quantity’s value in the provided unit.
### Comparing Quantities
- [func compare(HKQuantity) -> ComparisonResult](hkquantity/compare(_:).md)
  Compares two values after converting them to the same units.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Defining and converting units and quantities](defining-and-converting-units-and-quantities.md)
  Create and convert units and quantities.
- [class HKUnit](hkunit.md)
  A class for managing the units of measure within HealthKit.
- [enum HKMetricPrefix](hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantity)*