# NSMeasurement

**Framework**: Foundation  
**Kind**: class

A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class NSMeasurement
```

#### Overview

Use this object in Swift when you need reference semantics or other Foundation-specific behavior.

An [`NSMeasurement`](nsmeasurement.md) object represents a quantity and unit of measure. The [`NSMeasurement`](nsmeasurement.md) class provides a programmatic interface to converting measurements into different units, as well as calculating the sum or difference between two measurements.

[`NSMeasurement`](nsmeasurement.md) objects are initialized with an [`Unit`](unit.md) object and `double` value. [`NSMeasurement`](nsmeasurement.md) objects are immutable, and cannot be changed after being created.

You can use the [`MeasurementFormatter`](measurementformatter.md) class to create localized string representations of [`NSMeasurement`](nsmeasurement.md) objects.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Measurement`](measurement.md) structure, which bridges to the [`NSMeasurement`](nsmeasurement.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`Measurement`](measurement.md) structure, which bridges to the [`NSMeasurement`](nsmeasurement.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating Measurements
- [init(doubleValue: Double, unit: Unit)](nsmeasurement/init(doublevalue:unit:).md)
  Initializes a new measurement with a specified double-precision floating-point value and unit.
### Accessing Unit and Value
- [var unit: Unit](nsmeasurement/unit.md)
  The unit of measure.
- [var doubleValue: Double](nsmeasurement/doublevalue.md)
  The measurement value, represented as a double-precision floating-point number.
### Converting to Other Units
- [func canBeConverted(to: Unit) -> Bool](nsmeasurement/canbeconverted(to:).md)
  Indicates whether the measurement can be converted to the given unit.
- [func converting(to: Unit) -> Measurement<Unit>](nsmeasurement/converting(to:).md)
  Returns a measurement created by converting the receiver to the specified unit.
### Operating on Measurements
- [func adding(Measurement<Unit>) -> Measurement<Unit>](nsmeasurement/adding(_:).md)
  Returns a new measurement by adding the receiver to the specified measurement.
- [func subtracting(Measurement<Unit>) -> Measurement<Unit>](nsmeasurement/subtracting(_:).md)
  Returns a new measurement by subtracting the specified measurement from the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [struct Measurement](measurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Unit](unit.md)
  An abstract class representing a unit of measure.
- [class Dimension](dimension.md)
  An abstract class representing a dimensional unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmeasurement)*