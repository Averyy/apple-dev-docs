# HKMetricPrefix

**Framework**: HealthKit  
**Kind**: enum

Prefixes that can be added to SI units to change the order of magnitude.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKMetricPrefix
```

## Topics

### Prefixes
- [HKMetricPrefix.none](hkmetricprefix/none.md)
  A prefix that does not modify the base unit.
- [HKMetricPrefix.femto](hkmetricprefix/femto.md)
  A prefix that multiplies the base unit by 1e-15.
- [HKMetricPrefix.pico](hkmetricprefix/pico.md)
  A prefix that multiplies the base unit by 1e-12.
- [HKMetricPrefix.nano](hkmetricprefix/nano.md)
  A prefix that multiplies the base unit by 1e-9.
- [HKMetricPrefix.micro](hkmetricprefix/micro.md)
  A prefix that multiplies the base unit by 1e-6.
- [HKMetricPrefix.milli](hkmetricprefix/milli.md)
  A prefix that multiplies the base unit by 0.001.
- [HKMetricPrefix.centi](hkmetricprefix/centi.md)
  A prefix that multiplies the base unit by 0.01.
- [HKMetricPrefix.deci](hkmetricprefix/deci.md)
  A prefix that multiplies the base unit by 0.1.
- [HKMetricPrefix.deca](hkmetricprefix/deca.md)
  A prefix that multiplies the base unit by 10.
- [HKMetricPrefix.hecto](hkmetricprefix/hecto.md)
  A prefix that multiplies the base unit by 100.
- [HKMetricPrefix.kilo](hkmetricprefix/kilo.md)
  A prefix that multiplies the base unit by 1000.
- [HKMetricPrefix.mega](hkmetricprefix/mega.md)
  A prefix that multiplies the base unit by 1e6.
- [HKMetricPrefix.giga](hkmetricprefix/giga.md)
  A prefix that multiplies the base unit by 1e9.
- [HKMetricPrefix.tera](hkmetricprefix/tera.md)
  A prefix that multiplies the base unit by 1e12.
### Initializers
- [init?(rawValue: Int)](hkmetricprefix/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Defining and converting units and quantities](defining-and-converting-units-and-quantities.md)
  Create and convert units and quantities.
- [class HKQuantity](hkquantity.md)
  An object that stores a value for a given unit.
- [class HKUnit](hkunit.md)
  A class for managing the units of measure within HealthKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetricprefix)*