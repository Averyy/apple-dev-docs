# literUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring volume, using liter units with the provided prefix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func literUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) literUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

#### Return Value

A HealthKit unit for measuring volume based on liters and the provided prefix.

#### Discussion

This method is used to create prefixed versions of liters, typically milliliter units, as shown below.

**Swift**:

```swift
let ml = HKUnit.literUnitWithMetricPrefix(.Milli)
let ml = HKUnit.literUnitWithMetricPrefix(.Milli)
```

**Objective-C**:

```objc
HKUnit *ml = [HKUnit literUnitWithMetricPrefix:HKMetricPrefixMilli];
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing volume units
- [class func liter() -> Self](./liter%28%29.md)
  Returns a HealthKit unit for measuring volume in liters.
- [class func fluidOunceUS() -> Self](./fluidounceus%28%29.md)
  Returns a HealthKit unit for measuring volume in US fluid ounces.
- [class func fluidOunceImperial() -> Self](./fluidounceimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial fluid ounces.
- [class func cupUS() -> Self](./cupus%28%29.md)
  Returns a HealthKit unit for measuring volume in US cups.
- [class func cupImperial() -> Self](./cupimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial cups.
- [class func pintUS() -> Self](./pintus%28%29.md)
  Returns a HealthKit unit for measuring volume in US pints.
- [class func pintImperial() -> Self](./pintimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial pints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/literunit(with:))*