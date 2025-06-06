# containerView

**Framework**: UIKit  
**Kind**: property

The view in which the presentation occurs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var containerView: UIView? { get }
```

#### Discussion

UIKit sets the value of this property shortly after receiving the presentation controller from your transitioning delegate. The container view is always an ancestor of the presented view controller’s view. During transition animations, the container view also contains the presenting view controller’s view. When adding custom views to a presentation, add them to the container view.

If your transition also employs custom animator objects, those objects can get this container view from the [`containerView`](uiviewcontrollercontexttransitioning/containerview.md) property of the context object provided by UIKit.

## See Also

- [var presentingViewController: UIViewController](uipresentationcontroller/presentingviewcontroller.md)
  The view controller that is the starting point for the presentation.
- [var presentedViewController: UIViewController](uipresentationcontroller/presentedviewcontroller.md)
  The view controller being presented.
- [var presentedView: UIView?](uipresentationcontroller/presentedview.md)
  The view to be animated by the animator objects during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/containerview)*