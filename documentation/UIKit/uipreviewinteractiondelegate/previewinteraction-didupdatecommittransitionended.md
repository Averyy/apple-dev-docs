# previewInteraction(_:didUpdateCommitTransition:ended:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate of the preview interaction’s progress through the commit phase.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdateCommitTransition transitionProgress: CGFloat, ended: Bool)
```

#### Discussion

This method is called repeatedly during the commit phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the  effect in view controller preview transitions progressively increases the size of the child view controller as the transition progresses.

The `ended` parameter is false throughout the commit phase and becomes [`true`](https://developer.apple.com/documentation/Swift/true) when the phase is completed. At this point, the preview interaction is complete, and you should update the UI appropriately. For example, in view controller preview interactions, the child view controller becomes the main view controller.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.
- `transitionProgress`: The progress through the commit phase of the transition. A   with a value from   to  .
- `ended`: A   whose value indicates whether the commit phase of the transition is complete.

## See Also

- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](uipreviewinteractiondelegate/previewinteractionshouldbegin(_:).md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:).md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteractionDidCancel(UIPreviewInteraction)](uipreviewinteractiondelegate/previewinteractiondidcancel(_:).md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:))*