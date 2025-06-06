# jouleUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring energy, using joule units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func jouleUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring energy based on joules and the provided prefix.

#### Discussion

This method is used to create prefixed versions of joules. HealthKit commonly uses kilojoules to measure food energy in many regions. Kilojoules can be created as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func joule() -> Self](hkunit/joule.md)
  Returns a HealthKit unit for measuring energy in joules.
- [class func kilocalorie() -> Self](hkunit/kilocalorie.md)
  Returns a HealthKit unit for measuring energy in kilocalories.
- [class func largeCalorie() -> Self](hkunit/largecalorie.md)
  Returns a HealthKit unit for measuring energy in large calories (Cal).
- [class func smallCalorie() -> Self](hkunit/smallcalorie.md)
  Returns a HealthKit unit for measuring energy in small calories (cal).
- [class func calorie() -> Self](hkunit/calorie.md)
  Returns a HealthKit unit for measuring energy in calories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/jouleunit(with:))*