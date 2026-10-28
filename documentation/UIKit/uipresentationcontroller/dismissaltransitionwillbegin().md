# dismissalTransitionWillBegin()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the presentation controller that the dismissal animations are about to start.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func dismissalTransitionWillBegin()
```

```objc
- (void) dismissalTransitionWillBegin;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to configure any animations associated with your presentation’s custom views. To perform your animations, get the transition coordinator of the presented view controller and call its [`animate(alongsideTransition:completion:)`](../uiviewcontrollertransitioncoordinator/animate%28alongsidetransition,completion%29.md) or [`animateAlongsideTransition(in:animation:completion:)`](../uiviewcontrollertransitioncoordinator/animatealongsidetransition%28in,animation,completion%29.md) method. Calling those methods ensures that your animations are executed at the same time as any other transition animations.

Do not use this method to remove your views from the view hierarchy. Remove your views in the [`dismissalTransitionDidEnd(_:)`](./dismissaltransitiondidend%28_%29.md) method instead.

## See Also

### Tracking the transition’s start and end
- [func presentationTransitionWillBegin()](./presentationtransitionwillbegin%28%29.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func presentationTransitionDidEnd(Bool)](./presentationtransitiondidend%28_%29.md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionDidEnd(Bool)](./dismissaltransitiondidend%28_%29.md)
  Notifies the presentation controller that the dismissal animations finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitionwillbegin())*