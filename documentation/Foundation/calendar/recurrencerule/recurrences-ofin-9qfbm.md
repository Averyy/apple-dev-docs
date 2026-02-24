# recurrences(of:in:)

**Framework**: Foundation  
**Kind**: method

Find recurrences of the given date

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
func recurrences(of start: Date, in range: PartialRangeThrough<Date>) -> some Sendable & Sequence<Date>
```

#### Return Value

A sequence of dates conforming to the recurrence rule, in the given `range`. An empty sequence if the rule doesn’t match any dates.

#### Discussion

The calculations are implemented according to RFC-5545 and RFC-7529.

## Parameters

- `start`: The date which defines the starting point for the recurrence rule.
- `range`: A range of dates which to search for recurrences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/recurrences(of:in:)-9qfbm)*