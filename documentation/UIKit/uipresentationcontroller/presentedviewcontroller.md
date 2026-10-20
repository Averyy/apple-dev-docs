# presentedViewController

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view controller being presented.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var presentedViewController: UIViewController { get }
```

```objc
@property (nonatomic, strong, readonly) UIViewController * presentedViewController;
```

#### Discussion

This object corresponds to the one passed as the first parameter of the [`present(_:animated:completion:)`](../uiviewcontroller/present%28_,animated,completion%29.md) method. The successful conclusion of the presentation process causes this view controller’s content to be displayed onscreen.

## See Also

### Getting the presentation objects
- [var presentingViewController: UIViewController](./presentingviewcontroller.md)
  The view controller that is the starting point for the presentation.
- [var containerView: UIView?](./containerview.md)
  The view in which the presentation occurs.
- [var presentedView: UIView?](./presentedview.md)
  The view to be animated by the animator objects during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentedviewcontroller)*