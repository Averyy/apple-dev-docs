# HKQuantity

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKQuantity : NSObject
```

## Mentions

- [Defining and converting units and quantities](./defining-and-converting-units-and-quantities.md)
- [Saving data to HealthKit](./saving-data-to-healthkit.md)

## Overview

HealthKit uses quantity objects to store numerical data. When you create a quantity, you provide both the quantity’s value and unit.

Quantities are immutable objects: Their values are set when the object is first created and cannot change.

### Converting Units

You can request the value from a quantity object in any compatible units. For example,  if you create a length quantity in feet, you can then request the length in meters. The quantity object automatically converts its value to the requested units.

### Using Quantities

As with many HealthKit classes, don’t subclass the [`HKQuantity`](./hkquantity.md) class. To help promote sharing data between apps, [`HKQuantity`](./hkquantity.md) objects use only the units defined by the [`HKUnit`](./hkunit.md) class.

## Topics

### Creating Quantities
- [convenience init(unit: HKUnit, doubleValue: Double)](./hkquantity/init%28unit,doublevalue%29.md)
  Instantiates and returns a new quantity object.
### Working With Units
- [func `is`(compatibleWith: HKUnit) -> Bool](./hkquantity/is%28compatiblewith%29.md)
  Returns a boolean value indicating whether the quantity is compatible with the provided unit.
- [func doubleValue(for: HKUnit) -> Double](./hkquantity/doublevalue%28for%29.md)
  Returns the quantity’s value in the provided unit.
### Comparing Quantities
- [func compare(HKQuantity) -> ComparisonResult](./hkquantity/compare%28_%29.md)
  Compares two values after converting them to the same units.
### Initializers
- [init?(coder: NSCoder)](./hkquantity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Units and quantities
- [Defining and converting units and quantities](./defining-and-converting-units-and-quantities.md)
  Create and convert units and quantities.
- [class HKUnit](./hkunit.md)
  A class for managing the units of measure within HealthKit.
- [enum HKMetricPrefix](./hkmetricprefix.md)
  Prefixes that can be added to SI units to change the order of magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantity)*