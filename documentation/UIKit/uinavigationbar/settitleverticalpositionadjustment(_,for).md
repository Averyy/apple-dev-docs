# setTitleVerticalPositionAdjustment(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the title’s vertical position adjustment for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTitleVerticalPositionAdjustment(_ adjustment: CGFloat, for barMetrics: UIBarMetrics)
```

```objc
- (void) setTitleVerticalPositionAdjustment:(CGFloat) adjustment forBarMetrics:(UIBarMetrics) barMetrics;
```

## Parameters

- `adjustment`: The title’s vertical position adjustment for `barMetrics`.
- `barMetrics`: A bar metrics constant.

## See Also

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]?](./titletextattributes.md)
  Display attributes for the bar’s title text.
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]?](./largetitletextattributes.md)
  Display attributes for the bar’s large title text.
- [func titleVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./titleverticalpositionadjustment%28for%29.md)
  Returns the title’s vertical position adjustment for given bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/settitleverticalpositionadjustment(_:for:))*