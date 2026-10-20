# previewInteractionDidCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate that the specified preview interaction was canceled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func previewInteractionDidCancel(_ previewInteraction: UIPreviewInteraction)
```

```objc
- (void) previewInteractionDidCancel:(UIPreviewInteraction *) previewInteraction;
```

#### Discussion

This method is called when the preview interaction is canceled, either programmatically through the [`cancel()`](../uipreviewinteraction/cancel%28%29.md) method on [`UIPreviewInteraction`](../uipreviewinteraction.md), or by interrupting the preview interaction before the commit phase is complete.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.

## See Also

### Managing preview interactions
- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](./previewinteractionshouldbegin%28_%29.md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatepreviewtransition,ended%29.md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatecommittransition,ended%29.md)
  Informs the delegate of the preview interaction’s progress through the commit phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractiondidcancel(_:))*