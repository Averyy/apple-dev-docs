# presentationTransitionWillBegin()

**Framework**: UIKit  
**Kind**: method

Notifies the presentation controller that the presentation animations are about to start.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationTransitionWillBegin()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to add custom views to the view hierarchy and to create any animations associated with those views. To perform your animations, get the transition coordinator of the presented view controller and call its [`animate(alongsideTransition:completion:)`](uiviewcontrollertransitioncoordinator/animate(alongsidetransition:completion:).md) or [`animateAlongsideTransition(in:animation:completion:)`](uiviewcontrollertransitioncoordinator/animatealongsidetransition(in:animation:completion:).md) method. Calling those methods ensures that your animations are executed at the same time as any other transition animations.

For an example of how to implement this method, see [`Add custom views to a presentation`](uipresentationcontroller#Add-custom-views-to-a-presentation.md).

## See Also

- [func presentationTransitionDidEnd(Bool)](uipresentationcontroller/presentationtransitiondidend(_:).md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionWillBegin()](uipresentationcontroller/dismissaltransitionwillbegin.md)
  Notifies the presentation controller that the dismissal animations are about to start.
- [func dismissalTransitionDidEnd(Bool)](uipresentationcontroller/dismissaltransitiondidend(_:).md)
  Notifies the presentation controller that the dismissal animations finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationtransitionwillbegin())*