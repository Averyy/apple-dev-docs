# second()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a HealthKit unit for measuring time in seconds.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func second() -> Self
```

```objc
+ (instancetype) secondUnit;
```

#### Return Value

A HealthKit unit for measuring time in seconds.

## See Also

### Constructing time units
- [class func secondUnit(with: HKMetricPrefix) -> Self](./secondunit%28with%29.md)
  Returns a HealthKit unit for measuring time, using second units with the provided prefix.
- [class func minute() -> Self](./minute%28%29.md)
  Returns a HealthKit unit for measuring time in minutes.
- [class func hour() -> Self](./hour%28%29.md)
  Returns a HealthKit unit for measuring time in hours.
- [class func day() -> Self](./day%28%29.md)
  Returns a HealthKit unit for measuring time in days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/second())*