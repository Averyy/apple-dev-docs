# dates(byMatching:startingAt:in:matchingPolicy:repeatedTimePolicy:direction:)

**Framework**: Foundation  
**Kind**: method

Computes the dates which match (or most closely match) a given set of components, returned as a `Sequence`.

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
func dates(byMatching components: DateComponents, startingAt start: Date, in range: Range<Date>? = nil, matchingPolicy: Calendar.MatchingPolicy = .nextTime, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, direction: Calendar.SearchDirection = .forward) -> some Sendable & Sequence<Date>
```

#### Discussion

If `direction` is set to `.backward`, this method finds the previous match before the start date. The intent is that the same matches as for a `.forward` search will be found. For example, if you are searching forwards or backwards for each hour with minute “27”, the seconds in the date you will get in both a `.forward` and `.backward` search would be `00`.  Similarly, for DST backwards jumps which repeat times, you’ll get the first match by default, where “first” is defined from the point of view of searching forwards. Therefore, when searching backwards looking for a particular hour, with no minute and second specified, you don’t get a minute and second of `59:59` for the matching hour but instead `00:00`.

If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.

If an exact match is not possible, and requested with the `strict` option, the sequence ends.

Result dates have an integer number of seconds (as if 0 was specified for the nanoseconds property of the `DateComponents` matching parameter), unless a value was set in the nanoseconds property, in which case the result date will have that number of nanoseconds, or as close as possible with floating point numbers.

## Parameters

- `components`: The   to use as input to the search algorithm.
- `start`: The   at which to start the search.
- `range`: The range of dates to allow in the result. The sequence terminates if the next result is not contained in this range. If  , all results are allowed.
- `matchingPolicy`: Determines the behavior of the search algorithm when the input produces an ambiguous result.
- `repeatedTimePolicy`: Determines the behavior of the search algorithm when the input produces a time that occurs twice on a particular day.
- `direction`: Which direction in time to search. The default value is  , which means later in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dates(bymatching:startingat:in:matchingpolicy:repeatedtimepolicy:direction:))*