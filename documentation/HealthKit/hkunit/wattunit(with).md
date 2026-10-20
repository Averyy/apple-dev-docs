# wattUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring power, using watt units with the provided prefix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func wattUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) wattUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing power units
- [class func watt() -> Self](./watt%28%29.md)
  Returns a HealthKit unit for measuring power in watts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/wattunit(with:))*