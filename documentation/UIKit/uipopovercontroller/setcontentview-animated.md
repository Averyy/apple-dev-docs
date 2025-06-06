# setContentView(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the view controller responsible for the content portion of the popover.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func setContentView(_ viewController: UIViewController, animated: Bool)
```

## Parameters

- `viewController`: The new view controller whose content should be displayed by the popover.
- `animated`: Specify   if the change of view controllers should be animated or   if the change should occur immediately.

## See Also

- [var contentViewController: UIViewController](uipopovercontroller/contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](uipopovercontroller/contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](uipopovercontroller/setcontentsize(_:animated:).md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](uipopovercontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/setcontentview(_:animated:))*