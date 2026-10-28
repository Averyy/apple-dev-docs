# largeCalorie()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring energy in large calories (Cal).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func largeCalorie() -> Self
```

```objc
+ (instancetype) largeCalorieUnit;
```

## Discussion

The large calorie is the same as a kilocalorie (1 Cal = 4184.0 J).

## See Also

### Constructing energy units
- [class func joule() -> Self](./joule%28%29.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](./jouleunit%28with%29.md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](./kilocalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func smallCalorie() -> Self](./smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](./calorie%28%29.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/largecalorie())*