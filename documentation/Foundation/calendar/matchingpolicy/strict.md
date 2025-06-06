# Calendar.MatchingPolicy.strict

**Framework**: Foundation  
**Kind**: case

If specified, the algorithm travels as far forward or backward as necessary looking for a match.

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
case strict
```

#### Discussion

For example, if searching for Feb 29 in the Gregorian calendar, the algorithm may choose March 1 instead (for example, if the year is not a leap year). If you wish to find the next Feb 29 without the algorithm adjusting the next higher component in the specified `DateComponents`, then use the `strict` option.

> **Note**:  There are ultimately implementation-defined limits in how far distant the search will go.

 There are ultimately implementation-defined limits in how far distant the search will go.

## See Also

- [Calendar.MatchingPolicy.nextTime](calendar/matchingpolicy/nexttime.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the next existing time which exists.
- [Calendar.MatchingPolicy.nextTimePreservingSmallerComponents](calendar/matchingpolicy/nexttimepreservingsmallercomponents.md)
  If specified, and there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the method returns the next existing value of the missing component and preserves the lower components’ values (for example, no 2:37am results in 3:37am, if that exists).
- [Calendar.MatchingPolicy.previousTimePreservingSmallerComponents](calendar/matchingpolicy/previoustimepreservingsmallercomponents.md)
  If there is no matching time before the end of the next instance of the next higher component to the highest specified component in the `DateComponents` argument, the algorithm will return the previous existing value of the missing component and preserves the lower components’ values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/matchingpolicy/strict)*