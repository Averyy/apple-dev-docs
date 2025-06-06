# contentViewController

**Framework**: UIKit  
**Kind**: property

The view controller responsible for the content portion of the popover.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var contentViewController: UIViewController { get set }
```

#### Discussion

This property is initially set to the view controller passed to the [`init(contentViewController:)`](uipopovercontroller/init(contentviewcontroller:).md) method. You can change the value of this property later to reflect a new set of content. Changing the value of this property swaps the new view controller in for the old one immediately and does not trigger an animation. If you want to animate the change, use the [`setContentView(_:animated:)`](uipopovercontroller/setcontentview(_:animated:).md) method instead.

## See Also

- [func setContentView(UIViewController, animated: Bool)](uipopovercontroller/setcontentview(_:animated:).md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](uipopovercontroller/contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](uipopovercontroller/setcontentsize(_:animated:).md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](uipopovercontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/contentviewcontroller)*