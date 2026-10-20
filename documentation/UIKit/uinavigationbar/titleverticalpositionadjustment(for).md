# titleVerticalPositionAdjustment(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the title’s vertical position adjustment for given bar metrics.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func titleVerticalPositionAdjustment(for barMetrics: UIBarMetrics) -> CGFloat
```

```objc
- (CGFloat) titleVerticalPositionAdjustmentForBarMetrics:(UIBarMetrics) barMetrics;
```

#### Return Value

The title’s vertical position adjustment for `barMetrics`.

## Parameters

- `barMetrics`: A bar metrics constant.

## See Also

### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]?](./titletextattributes.md)
  Display attributes for the bar’s title text.
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]?](./largetitletextattributes.md)
  Display attributes for the bar’s large title text.
- [func setTitleVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./settitleverticalpositionadjustment%28_,for%29.md)
  Sets the title’s vertical position adjustment for given bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/titleverticalpositionadjustment(for:))*