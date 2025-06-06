# Calendar.RepeatedTimePolicy.last

**Framework**: Foundation  
**Kind**: case

If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the last occurrence.

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
case last
```

## See Also

- [Calendar.RepeatedTimePolicy.first](calendar/repeatedtimepolicy/first.md)
  If there are two or more matching times (all the components are the same, including isLeapMonth) before the end of the next instance of the next higher component to the highest specified component, then the algorithm will return the first occurrence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/repeatedtimepolicy/last)*