# voltUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring the electrical potential difference in volts with the provided prefix.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func voltUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) voltUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Electrical potential difference
- [class func volt() -> Self](./volt%28%29.md)
  Returns a HealthKit unit for measuring the difference in electrical potential using volts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/voltunit(with:))*