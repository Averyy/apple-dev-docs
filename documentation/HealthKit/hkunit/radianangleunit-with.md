# radianAngleUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring angles, using radian units with the provided prefix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func radianAngleUnit(with prefix: HKMetricPrefix) -> Self
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func degreeAngle() -> Self](hkunit/degreeangle.md)
  Returns a HealthKit unit for measuring angles using degrees.
- [class func radianAngle() -> Self](hkunit/radianangle.md)
  Returns a HealthKit unit for measuring angles using radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/radianangleunit(with:))*