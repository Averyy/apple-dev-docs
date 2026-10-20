# dismissalTransitionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the presentation controller that the dismissal animations finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func dismissalTransitionDidEnd(_ completed: Bool)
```

```objc
- (void) dismissalTransitionDidEnd:(BOOL) completed;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to remove any custom views that the presentation controller added to the view hierarchy. Remove your views only if the `completed` parameter is [`true`](../../Swift/true.md).

## Parameters

- `completed`: [`true`](../../Swift/true.md) if the animations completed and the presented view controller was dismissed or [`false`](../../Swift/false.md) if the animations were canceled and the presented view controller is still visible.

## See Also

### Tracking the transition’s start and end
- [func presentationTransitionWillBegin()](./presentationtransitionwillbegin%28%29.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func presentationTransitionDidEnd(Bool)](./presentationtransitiondidend%28_%29.md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionWillBegin()](./dismissaltransitionwillbegin%28%29.md)
  Notifies the presentation controller that the dismissal animations are about to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitiondidend(_:))*