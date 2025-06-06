# setContentSize(_:animated:)

**Framework**: UIKit  
**Kind**: method

Changes the size of the popover’s content view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func setContentSize(_ size: CGSize, animated: Bool)
```

#### Discussion

When changing the size of the popover’s content, the width value you specify must be at least 320 points and no more than 600 points. There are no restrictions on the height value. However, both the width and height values you specify may be adjusted to ensure the popup fits on screen and is not covered by the keyboard.

## Parameters

- `size`: The new size to apply to the content view.
- `animated`: Specify   if you want the change in size to be animated or   if you want the change to appear immediately.

## See Also

- [var contentViewController: UIViewController](uipopovercontroller/contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [func setContentView(UIViewController, animated: Bool)](uipopovercontroller/setcontentview(_:animated:).md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](uipopovercontroller/contentsize.md)
  The size of the popover’s content view.
- [var passthroughViews: [UIView]?](uipopovercontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/setcontentsize(_:animated:))*