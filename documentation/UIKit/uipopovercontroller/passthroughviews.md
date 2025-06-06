# passthroughViews

**Framework**: UIKit  
**Kind**: property

An array of views that the user can interact with while the popover is visible.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var passthroughViews: [UIView]? { get set }
```

#### Discussion

When a popover is active, interactions with other views are normally disabled until the popover is dismissed. Assigning an array of views to this property allows taps outside of the popover to be handled by the corresponding views.

## See Also

- [var contentViewController: UIViewController](uipopovercontroller/contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [func setContentView(UIViewController, animated: Bool)](uipopovercontroller/setcontentview(_:animated:).md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](uipopovercontroller/contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](uipopovercontroller/setcontentsize(_:animated:).md)
  Changes the size of the popover’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/passthroughviews)*