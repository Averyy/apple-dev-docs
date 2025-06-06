# secondUnit(with:)

**Framework**: HealthKit  
**Kind**: method

Returns a HealthKit unit for measuring time, using second units with the provided prefix.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func secondUnit(with prefix: HKMetricPrefix) -> Self
```

#### Return Value

A HealthKit unit for measuring time based on seconds and the provided prefix.

#### Discussion

This method is used to create prefixed versions of seconds. Common uses include creating millisecond units, as shown below.

## Parameters

- `prefix`: A valid metric prefix value. For the complete list of prefix values, see  .

## See Also

- [class func second() -> Self](hkunit/second.md)
  Returns a HealthKit unit for measuring time in seconds.
- [class func minute() -> Self](hkunit/minute.md)
  Returns a HealthKit unit for measuring time in minutes.
- [class func hour() -> Self](hkunit/hour.md)
  Returns a HealthKit unit for measuring time in hours.
- [class func day() -> Self](hkunit/day.md)
  Returns a HealthKit unit for measuring time in days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkunit/secondunit(with:))*