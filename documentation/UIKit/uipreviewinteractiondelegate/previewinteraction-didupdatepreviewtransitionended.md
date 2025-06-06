# previewInteraction(_:didUpdatePreviewTransition:ended:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the delegate of the progress through the preview phase of the preview interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdatePreviewTransition transitionProgress: CGFloat, ended: Bool)
```

#### Discussion

This method is called repeatedly during the preview phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the  effect in view controller preview transitions progressively blurs everything except the appropriate view.

The `ended` parameter is [`false`](https://developer.apple.com/documentation/swift/false) throughout the preview phase and becomes [`true`](https://developer.apple.com/documentation/swift/true) as the phase is completed. The preview interaction then transitions to the commit phase, so you should use this point to update the UI as required.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.
- `transitionProgress`: The progress through the preview phase of the transition. A   with a value from   to  .
- `ended`: A Boolean whose value indicates whether the preview phase of the transition is complete.

## See Also

- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](uipreviewinteractiondelegate/previewinteractionshouldbegin(_:).md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:).md)
  Informs the delegate of the preview interaction’s progress through the commit phase.
- [func previewInteractionDidCancel(UIPreviewInteraction)](uipreviewinteractiondelegate/previewinteractiondidcancel(_:).md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:))*