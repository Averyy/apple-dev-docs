# dates(byAdding:startingAt:in:wrappingComponents:)

**Framework**: Foundation  
**Kind**: method

Returns a sequence of `Date`s, calculated by repeatedly adding an amount of `DateComponents` to a starting `Date` and then to each subsequent result. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.

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
func dates(byAdding components: DateComponents, startingAt start: Date, in range: Range<Date>? = nil, wrappingComponents: Bool = false) -> some Sendable & Sequence<Date>
```

#### Return Value

A `Sequence` of `Date` values, or an empty sequence if no addition could be performed.

## Parameters

- `components`: The components to add or subtract.
- `start`: The starting point of the search.
- `range`: The range of dates to allow in the result. The sequence terminates if the next result is not contained in this range. If  , all results are allowed.
- `wrappingComponents`: If  , the component should be incremented and wrap around to zero/one on overflow, and should not cause higher components to be incremented. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dates(byadding:startingat:in:wrappingcomponents:))*