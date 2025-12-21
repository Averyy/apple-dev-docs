# recurrences(of:in:)

**Framework**: Foundation  
**Kind**: method

Find recurrences of the given date

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func recurrences(of start: Date, in range: Range<Date>? = nil) -> some Sendable & Sequence<Date>
```

#### Return Value

A sequence of dates conforming to the recurrence rule, in the given `range`. An empty sequence if the rule doesn’t match any dates. A recurrence that repeats every `interval` minutes

#### Discussion

The calculations are implemented according to RFC-5545 and RFC-7529.

## Parameters

- `start`: The date which defines the starting point for the   recurrence rule.
- `range`: A range of dates which to search for recurrences.   If  , return all recurrences of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/recurrences(of:in:))*