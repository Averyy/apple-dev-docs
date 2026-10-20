# presentationTransitionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the presentation controller that the presentation animations finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func presentationTransitionDidEnd(_ completed: Bool)
```

```objc
- (void) presentationTransitionDidEnd:(BOOL) completed;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to perform any required cleanup. For example, if the completed parameter is [`false`](../../Swift/false.md), you would use this method to remove your presentation’s custom views from the view hierarchy.

For an example of how to implement this method, see [Add custom views to a presentation](../uipresentationcontroller.md#Add-custom-views-to-a-presentation).

## Parameters

- `completed`: [`true`](../../Swift/true.md) if the animations completed and the presented view controller is now visible or [`false`](../../Swift/false.md) if the animations were canceled and the presenting view controller is still visible.

## See Also

### Tracking the transition’s start and end
- [func presentationTransitionWillBegin()](./presentationtransitionwillbegin%28%29.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func dismissalTransitionWillBegin()](./dismissaltransitionwillbegin%28%29.md)
  Notifies the presentation controller that the dismissal animations are about to start.
- [func dismissalTransitionDidEnd(Bool)](./dismissaltransitiondidend%28_%29.md)
  Notifies the presentation controller that the dismissal animations finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationtransitiondidend(_:))*