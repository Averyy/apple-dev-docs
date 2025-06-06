# meterUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring length, using meter units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func meterUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring length based on meters and the provided prefix.

#### Discussion

This method is used to create prefixed versions of meters. Common uses include creating kilometer and centimeter units, as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func meter() -> Self](hkunit/meter.md)
  Returns a HealthKit unit for measuring length in meters.
- [class func inch() -> Self](hkunit/inch.md)
  Returns a HealthKit unit for measuring length in inches.
- [class func foot() -> Self](hkunit/foot.md)
  Returns a HealthKit unit for measuring length in feet.
- [class func yard() -> Self](hkunit/yard.md)
  Returns a HealthKit unit for measuring length in yards.
- [class func mile() -> Self](hkunit/mile.md)
  Returns a HealthKit unit for measuring length in miles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/meterunit(with:))*