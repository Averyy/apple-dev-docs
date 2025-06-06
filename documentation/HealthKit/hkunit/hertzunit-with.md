# hertzUnit(with:)

**Framework**: HealthKit  
**Kind**: method

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

#### Discussion

Hertz represent cycles per second.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func hertz() -> Self](hkunit/hertz.md)
  Returns a HealthKit unit for measuring frequency in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/hertzunit(with:))*