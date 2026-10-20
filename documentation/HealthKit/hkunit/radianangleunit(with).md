# radianAngleUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (instancetype) radianAngleUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing angle units
- [class func degreeAngle() -> Self](./degreeangle%28%29.md)
  Returns a HealthKit unit for measuring angles using degrees.
- [class func radianAngle() -> Self](./radianangle%28%29.md)
  Returns a HealthKit unit for measuring angles using radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/radianangleunit(with:))*