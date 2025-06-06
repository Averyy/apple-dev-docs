# init(unit:doubleValue:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a new quantity object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(unit: HKUnit, doubleValue value: Double)
```

#### Return Value

A newly instantiated quantity instance.

#### Discussion

HealthKit uses quantity objects to store data for quantity samples. For more information on using quantity objects, see [`HKQuantitySample`](hkquantitysample.md).

## Parameters

- `unit`: The units for the given value. This defines the set of compatible units. For example, if you create a quantity with a meter unit, it is compatible with any other length units.
- `value`: The value of this quantity, measured using the unit parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantity/init(unit:doublevalue:))*