# titlePositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method

Returns the title offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func titlePositionAdjustment(for barMetrics: UIBarMetrics) -> UIOffset
```

#### Return Value

The title offset for `barMetrics`.

#### Discussion

This offset is used to adjust the position of a title (if any) within a bordered bar button.

## Parameters

- `barMetrics`: Bar metrics.

## See Also

- [func setTitlePositionAdjustment(UIOffset, for: UIBarMetrics)](uibarbuttonitem/settitlepositionadjustment(_:for:).md)
  Sets the title offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/titlepositionadjustment(for:))*