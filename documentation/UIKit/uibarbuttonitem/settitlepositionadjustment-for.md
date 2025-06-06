# setTitlePositionAdjustment(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the title offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setTitlePositionAdjustment(_ adjustment: UIOffset, for barMetrics: UIBarMetrics)
```

#### Discussion

This offset is used to adjust the position of a title (if any) within a bordered bar button.

## Parameters

- `adjustment`: The title offset for  .
- `barMetrics`: Bar metrics.

## See Also

- [func titlePositionAdjustment(for: UIBarMetrics) -> UIOffset](uibarbuttonitem/titlepositionadjustment(for:).md)
  Returns the title offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/settitlepositionadjustment(_:for:))*