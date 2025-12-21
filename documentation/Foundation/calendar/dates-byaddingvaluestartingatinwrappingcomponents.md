# dates(byAdding:value:startingAt:in:wrappingComponents:)

**Framework**: Foundation  
**Kind**: method

Returns a sequence of `Date`s, calculated by adding a scaled amount of `Calendar.Component`s to a starting `Date`. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.

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
func dates(byAdding component: Calendar.Component, value: Int = 1, startingAt start: Date, in range: Range<Date>? = nil, wrappingComponents: Bool = false) -> some Sendable & Sequence<Date>
```

#### Return Value

A `Sequence` of `Date` values, or an empty sequence if no addition could be performed.

## Parameters

- `component`: A component to add or subtract.
- `value`: The value of the specified component to add or subtract. The default value is  . The value can be negative, which causes subtraction.
- `start`: The starting point of the search.
- `range`: The range of dates to allow in the result. The sequence terminates if the next result is not contained in this range. If  , all results are allowed.
- `wrappingComponents`: If  , the component should be incremented and wrap around to zero/one on overflow, and should not cause higher components to be incremented. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dates(byadding:value:startingat:in:wrappingcomponents:))*