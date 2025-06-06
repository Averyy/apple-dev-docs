# contentSize

**Framework**: UIKit  
**Kind**: property

The size of the popover’s content view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var contentSize: CGSize { get set }
```

#### Discussion

This property represents the size of the content view that is managed by the view controller in the [`contentViewController`](uipopovercontroller/contentviewcontroller.md) property. The initial value of this property is set to value in the view controller’s [`contentSizeForViewInPopover`](uiviewcontroller/contentsizeforviewinpopover.md) property. Changing the value of this property overrides the default value of the current view controller. The overridden value persists until you assign a new content view controller to the receiver. Thus, if you want to keep your overridden value, you must reassign it after changing the content view controller.

When changing the value of this property, the width value you specify must be at least 320 points and no more than 600 points. There are no restrictions on the height value. However, both the width and height values you specify may be adjusted to ensure the popup fits on screen and is not covered by the keyboard. If you change the value of this property while the popover is visible, the size change is animated.

## See Also

- [var contentViewController: UIViewController](uipopovercontroller/contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [func setContentView(UIViewController, animated: Bool)](uipopovercontroller/setcontentview(_:animated:).md)
  Sets the view controller responsible for the content portion of the popover.
- [func setContentSize(CGSize, animated: Bool)](uipopovercontroller/setcontentsize(_:animated:).md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](uipopovercontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/contentsize)*