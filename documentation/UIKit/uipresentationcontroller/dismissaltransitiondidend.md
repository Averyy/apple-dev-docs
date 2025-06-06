# dismissalTransitionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the presentation controller that the dismissal animations finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissalTransitionDidEnd(_ completed: Bool)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to remove any custom views that the presentation controller added to the view hierarchy. Remove your views only if the `completed` parameter is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `completed`:   if the animations completed and the presented view controller was dismissed or   if the animations were canceled and the presented view controller is still visible.

## See Also

- [func presentationTransitionWillBegin()](uipresentationcontroller/presentationtransitionwillbegin.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func presentationTransitionDidEnd(Bool)](uipresentationcontroller/presentationtransitiondidend(_:).md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionWillBegin()](uipresentationcontroller/dismissaltransitionwillbegin.md)
  Notifies the presentation controller that the dismissal animations are about to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitiondidend(_:))*