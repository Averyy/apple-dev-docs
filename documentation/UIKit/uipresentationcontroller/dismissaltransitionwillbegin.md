# dismissalTransitionWillBegin()

**Framework**: UIKit  
**Kind**: method

Notifies the presentation controller that the dismissal animations are about to start.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissalTransitionWillBegin()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to configure any animations associated with your presentation’s custom views. To perform your animations, get the transition coordinator of the presented view controller and call its [`animate(alongsideTransition:completion:)`](uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:).md) or [`animateAlongsideTransition(in:animation:completion:)`](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md) method. Calling those methods ensures that your animations are executed at the same time as any other transition animations.

Do not use this method to remove your views from the view hierarchy. Remove your views in the [`dismissalTransitionDidEnd(_:)`](uipresentationcontroller/dismissaltransitiondidend(_:).md) method instead.

## See Also

- [func presentationTransitionWillBegin()](uipresentationcontroller/presentationtransitionwillbegin.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func presentationTransitionDidEnd(Bool)](uipresentationcontroller/presentationtransitiondidend(_:).md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionDidEnd(Bool)](uipresentationcontroller/dismissaltransitiondidend(_:).md)
  Notifies the presentation controller that the dismissal animations finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitionwillbegin())*