# UIFloatRangeIsEqualToRange

**Framework**: UIKit  
**Kind**: func

Returns a Boolean indicating whether two float ranges are equivalent.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static BOOL UIFloatRangeIsEqualToRange(UIFloatRange range, UIFloatRange otherRange);
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifloatrangeisequaltorange)*