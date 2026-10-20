# cupUS()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring volume in US cups.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func cupUS() -> Self
```

```objc
+ (instancetype) cupUSUnit;
```

#### Return Value

A HealthKit unit for measuring volume in US cups.

## See Also

### Constructing volume units
- [class func liter() -> Self](./liter%28%29.md)
  Returns a HealthKit unit for measuring volume in liters.
- [class func literUnit(with: HKMetricPrefix) -> Self](./literunit%28with%29.md)
  Returns a HealthKit unit for measuring volume, using liter units with the provided prefix.
- [class func fluidOunceUS() -> Self](./fluidounceus%28%29.md)
  Returns a HealthKit unit for measuring volume in US fluid ounces.
- [class func fluidOunceImperial() -> Self](./fluidounceimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial fluid ounces.
- [class func cupImperial() -> Self](./cupimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial cups.
- [class func pintUS() -> Self](./pintus%28%29.md)
  Returns a HealthKit unit for measuring volume in US pints.
- [class func pintImperial() -> Self](./pintimperial%28%29.md)
  Returns a HealthKit unit for measuring volume in imperial pints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/cupus())*