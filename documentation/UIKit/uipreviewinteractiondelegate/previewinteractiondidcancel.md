# previewInteractionDidCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Informs the delegate that the specified preview interaction was canceled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func previewInteractionDidCancel(_ previewInteraction: UIPreviewInteraction)
```

#### Discussion

This method is called when the preview interaction is canceled, either programmatically through the [`cancel()`](uipreviewinteraction/cancel().md) method on [`UIPreviewInteraction`](uipreviewinteraction.md), or by interrupting the preview interaction before the commit phase is complete.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.

## See Also

- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](uipreviewinteractiondelegate/previewinteractionshouldbegin(_:).md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:).md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:).md)
  Informs the delegate of the preview interaction’s progress through the commit phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractiondidcancel(_:))*