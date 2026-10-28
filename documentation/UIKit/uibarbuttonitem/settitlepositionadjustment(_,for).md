# setTitlePositionAdjustment(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the title offset for specified bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTitlePositionAdjustment(_ adjustment: UIOffset, for barMetrics: UIBarMetrics)
```

```objc
- (void) setTitlePositionAdjustment:(UIOffset) adjustment forBarMetrics:(UIBarMetrics) barMetrics;
```

## Discussion

This offset is used to adjust the position of a title (if any) within a bordered bar button.

## Parameters

- `adjustment`: The title offset for `barMetrics`.
- `barMetrics`: Bar metrics.

## See Also

### Customizing the title placement
- [func titlePositionAdjustment(for: UIBarMetrics) -> UIOffset](./titlepositionadjustment%28for%29.md)
  Returns the title offset for specified bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/settitlepositionadjustment(_:for:))*