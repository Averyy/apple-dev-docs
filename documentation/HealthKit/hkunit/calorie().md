# calorie()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring energy in calories.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: To avoid confusion, use [`largeCalorie()`](./largecalorie%28%29.md) or [`smallCalorie()`](./smallcalorie%28%29.md) instead.

## Declaration

```swift
class func calorie() -> Self
```

```objc
+ (instancetype) calorieUnit;
```

#### Return Value

A HealthKit unit for measuring energy in calories.

## See Also

### Constructing energy units
- [class func joule() -> Self](./joule%28%29.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](./jouleunit%28with%29.md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](./kilocalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](./largecalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](./smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/calorie())*