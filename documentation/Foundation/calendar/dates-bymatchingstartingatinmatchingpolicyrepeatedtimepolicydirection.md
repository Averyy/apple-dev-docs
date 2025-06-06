# dates(byMatching:startingAt:in:matchingPolicy:repeatedTimePolicy:direction:)

**Framework**: Foundation  
**Kind**: method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/dates(bymatching:startingat:in:matchingpolicy:repeatedtimepolicy:direction:))*