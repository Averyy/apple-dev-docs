# kilocalorie()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring energy in kilocalories.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func kilocalorie() -> Self
```

```objc
+ (instancetype) kilocalorieUnit;
```

## Return Value

A HealthKit unit for measuring energy in kilocalories.

## Discussion

The kilocalorie is used to measure food energy in many regions.

## See Also

### Constructing energy units
- [class func joule() -> Self](./joule%28%29.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](./jouleunit%28with%29.md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func largeCalorie() -> Self](./largecalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](./smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](./calorie%28%29.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/kilocalorie())*