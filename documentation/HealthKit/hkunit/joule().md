# joule()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring energy in joules.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func joule() -> Self
```

```objc
+ (instancetype) jouleUnit;
```

## Return Value

A HealthKit unit for measuring energy in joules.

## See Also

### Constructing energy units
- [class func jouleUnit(with: HKMetricPrefix) -> Self](./jouleunit%28with%29.md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](./kilocalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](./largecalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](./smallcalorie%28%29.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](./calorie%28%29.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/joule())*