# intersection(with:)

**Framework**: Foundation  
**Kind**: method

Returns an interval that represents the interval where the given date interval and the current instance intersect.

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
func intersection(with dateInterval: DateInterval) -> DateInterval?
```

#### Discussion

In the event that there is no intersection, the method returns nil.

## See Also

- [func intersects(DateInterval) -> Bool](dateinterval/intersects(_:).md)
  Indicates whether this interval intersects the specified interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateinterval/intersection(with:))*