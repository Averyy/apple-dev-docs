# UIFloatRangeIsEqualToRange(_:_:)

**Framework**: UIKit  
**Kind**: func

Returns a Boolean indicating whether two float ranges are equivalent.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- Swift 1.0+

## Declaration

```swift
func UIFloatRangeIsEqualToRange(_ range: UIFloatRange, _ otherRange: UIFloatRange) -> Bool
```

#### Discussion

Two ranges are considered equal when their minimum values are the same and their maximum values are the same. In practice, the minimum and maximum values do not have to be exactly equal, but the difference between each pair of values must be less than `FLT_EPSILON`.

## Parameters

- `range`: The first range to compare.
- `otherRange`: The second range to compare.

## See Also

- [var isInfinite: Bool](uifloatrange/isinfinite.md)
  Returns a Boolean indicating whether the specified float range is infinitely large.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrangeisequaltorange(_:_:))*