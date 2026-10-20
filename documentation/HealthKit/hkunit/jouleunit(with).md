# jouleUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func jouleUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) jouleUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

#### Return Value

A HealthKit unit for measuring energy based on joules and the provided prefix.

#### Discussion

This method is used to create prefixed versions of joules. HealthKit commonly uses kilojoules to measure food energy in many regions. Kilojoules can be created as shown below.

**Swift**:

```swift
let kj = HKUnit.jouleUnitWithMetricPrefix(.Kilo)
```

**Objective-C**:

```objc
HKUnit *kj = [HKUnit jouleUnitWithMetricPrefix:HKMetricPrefixKilo];
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing energy units
- [class func joule() -> Self](./joule%28%29.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func kilocalorie() -> Self](./kilocalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](./largecalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](./smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](./calorie%28%29.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/jouleunit(with:))*