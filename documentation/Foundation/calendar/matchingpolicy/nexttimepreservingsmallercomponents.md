# Calendar.MatchingPolicy.nextTimePreservingSmallerComponents

**Framework**: Foundation  
**Kind**: case

If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case nextTimePreservingSmallerComponents
```

## See Also

- [Calendar.MatchingPolicy.nextTime](calendar/matchingpolicy/nexttime.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](calendar/matchingpolicy/previoustimepreservingsmallercomponents.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.
- [Calendar.MatchingPolicy.strict](calendar/matchingpolicy/strict.md)
  If specified, the algorithm travels as far forward or backward as necessary looking for a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/matchingpolicy/nexttimepreservingsmallercomponents)*