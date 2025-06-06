# presentedView

**Framework**: UIKit  
**Kind**: property

The view to be animated by the animator objects during a transition.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var presentedView: UIView? { get }
```

#### Return Value

The view to present. This view must be either the presented view controller’s view or an ancestor of that view.

#### Discussion

The default implementation of this method returns the presented view controller’s view. If you want to animate a different view, you may override this method and return that view. The view you specify must either be the presented view controller’s view or must be one of its ancestors.

The view returned by this method is given to the animator objects, which are responsible for animating it onscreen. The animator objects retrieve the view using the [`view(forKey:)`](uiviewcontrollercontexttransitioning/view(forkey:).md) method of the context object provided by UIKit.

UIKit calls this method multiple times during the course of a presentation, so your implementation should return the appropriate view as quickly as possible. Do not use this method to actually configure your view hierarchy. If you intend to return a custom view, configure your view hierarchy in the [`presentationTransitionWillBegin()`](uipresentationcontroller/presentationtransitionwillbegin().md) method.

## See Also

- [var presentingViewController: UIViewController](uipresentationcontroller/presentingviewcontroller.md)
  The view controller that is the starting point for the presentation.
- [var presentedViewController: UIViewController](uipresentationcontroller/presentedviewcontroller.md)
  The view controller being presented.
- [var containerView: UIView?](uipresentationcontroller/containerview.md)
  The view in which the presentation occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentedview)*