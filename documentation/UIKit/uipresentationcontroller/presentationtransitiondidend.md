# presentationTransitionDidEnd(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the presentation controller that the presentation animations finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationTransitionDidEnd(_ completed: Bool)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to perform any required cleanup. For example, if the completed parameter is [`false`](https://developer.apple.com/documentation/swift/false), you would use this method to remove your presentation’s custom views from the view hierarchy.

For an example of how to implement this method, see [`Add custom views to a presentation`](uipresentationcontroller#Add-custom-views-to-a-presentation.md).

## Parameters

- `completed`:   if the animations completed and the presented view controller is now visible or   if the animations were canceled and the presenting view controller is still visible.

## See Also

- [func presentationTransitionWillBegin()](uipresentationcontroller/presentationtransitionwillbegin.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func dismissalTransitionWillBegin()](uipresentationcontroller/dismissaltransitionwillbegin.md)
  Notifies the presentation controller that the dismissal animations are about to start.
- [func dismissalTransitionDidEnd(Bool)](uipresentationcontroller/dismissaltransitiondidend(_:).md)
  Notifies the presentation controller that the dismissal animations finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationtransitiondidend(_:))*