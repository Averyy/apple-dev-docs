# smallCalorie()

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring energy in small calories (cal).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func smallCalorie() -> Self
```

#### Discussion

This unit represents the gram calorie, or the amount of energy needed to raise 1 gram of water by 1 degree Celsius (1 cal = 4.1840 J).

This unit is occasionally used in chemistry and other sciences, but it should not be confused with the kilocalorie, or large calorie, which is  used for measuring food energy in many regions.

## See Also

- [class func joule() -> Self](hkunit/joule.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func jouleUnit(with: HKMetricPrefix) -> Self](hkunit/jouleunit(with:).md)
  Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.
- [class func kilocalorie() -> Self](hkunit/kilocalorie.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](hkunit/largecalorie.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func calorie() -> Self](hkunit/calorie.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/smallcalorie())*