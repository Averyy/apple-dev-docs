# meterUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring length, using meter units with the provided prefix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func meterUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) meterUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

## Return Value

A HealthKit unit for measuring length based on meters and the provided prefix.

## Discussion

This method is used to create prefixed versions of meters. Common uses include creating kilometer and centimeter units, as shown below.

**Swift**:

```swift
let km = HKUnit.meterUnitWithMetricPrefix(.Kilo)
let cm = HKUnit.meterUnitWithMetricPrefix(.Centi)
```

**Objective-C**:

```objc
HKUnit *km = [HKUnit meterUnitWithMetricPrefix:HKMetricPrefixKilo];
HKUnit *cm = [HKUnit meterUnitWithMetricPrefix:HKMetricPrefixCenti];
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing length units
- [class func meter() -> Self](./meter%28%29.md)
  Returns a HealthKit unit for measuring length in meters.
- [class func inch() -> Self](./inch%28%29.md)
  Returns a HealthKit unit for measuring length in inches.
- [class func foot() -> Self](./foot%28%29.md)
  Returns a HealthKit unit for measuring length in feet.
- [class func yard() -> Self](./yard%28%29.md)
  Returns a HealthKit unit for measuring length in yards.
- [class func mile() -> Self](./mile%28%29.md)
  Returns a HealthKit unit for measuring length in miles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/meterunit(with:))*