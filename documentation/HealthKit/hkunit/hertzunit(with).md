# hertzUnit(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring frequency in hertz with the provided prefix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func hertzUnit(with prefix: HKMetricPrefix) -> Self
```

```objc
+ (instancetype) hertzUnitWithMetricPrefix:(HKMetricPrefix) prefix;
```

#### Discussion

Hertz represent cycles per second.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see [`HKMetricPrefix`](../hkmetricprefix.md).

## See Also

### Constructing frequency units
- [class func hertz() -> Self](./hertz%28%29.md)
  Returns a HealthKit unit for measuring frequency in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/hertzunit(with:))*