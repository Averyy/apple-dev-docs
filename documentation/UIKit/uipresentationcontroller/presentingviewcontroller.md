# presentingViewController

**Framework**: UIKit  
**Kind**: property

The view controller that is the starting point for the presentation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var presentingViewController: UIViewController { get }
```

#### Discussion

The object in this property could be the root view controller of the window, a parent view controller that is marked as defining the current context, or the last view controller that was presented onscreen. This view controller may or may not be the same one whose [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method was called to initiate the presentation process. It may also not be the view controller used to initialize your presentation controller.

## See Also

- [var presentedViewController: UIViewController](uipresentationcontroller/presentedviewcontroller.md)
  The view controller being presented.
- [var containerView: UIView?](uipresentationcontroller/containerview.md)
  The view in which the presentation occurs.
- [var presentedView: UIView?](uipresentationcontroller/presentedview.md)
  The view to be animated by the animator objects during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentingviewcontroller)*