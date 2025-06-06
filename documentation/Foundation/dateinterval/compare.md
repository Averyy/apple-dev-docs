# compare(_:)

**Framework**: Foundation  
**Kind**: method

Compares two intervals.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func compare(_ dateInterval: DateInterval) -> ComparisonResult
```

#### Discussion

This method prioritizes ordering by start date. If the start dates are equal, then it will order by duration. e.g. Given intervals a and b

```swift
a.   |-----|
b.      |-----|
```

`a.compare(b)` would return `.OrderedAscending` because a’s start date is earlier in time than b’s start date.

In the event that the start dates are equal, the compare method will attempt to order by duration. e.g. Given intervals c and d

```swift
c.  |-----|
d.  |---|
```

`c.compare(d)` would result in `.OrderedDescending` because c is longer than d.

If both the start dates and the durations are equal, then the intervals are considered equal and `.OrderedSame` is returned as the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateinterval/compare(_:))*