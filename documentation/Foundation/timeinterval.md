# TimeInterval

**Framework**: Foundation  
**Kind**: typealias

A number of seconds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias TimeInterval = Double
```

#### Discussion

A [`TimeInterval`](timeinterval.md) value is always specified in seconds; it yields sub-millisecond precision over a range of 10,000 years.

On its own, a time interval does not specify a unique point in time, or even a span between specific times. Combining a time interval with one or more known reference points yields a [`Date`](date.md) or [`DateInterval`](dateinterval.md) value.

## See Also

- [struct Date](date.md)
  A specific point in time, independent of any calendar or time zone.
- [struct DateInterval](dateinterval.md)
  The span of time between a specific start date and end date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timeinterval)*