# previewInteraction(_:didUpdateCommitTransition:ended:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate of the preview interaction’s progress through the commit phase.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdateCommitTransition transitionProgress: CGFloat, ended: Bool)
```

```objc
- (void) previewInteraction:(UIPreviewInteraction *) previewInteraction didUpdateCommitTransition:(CGFloat) transitionProgress ended:(BOOL) ended;
```

## Discussion

This method is called repeatedly during the commit phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the *pop* effect in view controller preview transitions progressively increases the size of the child view controller as the transition progresses.

The `ended` parameter is false throughout the commit phase and becomes [`true`](../../Swift/true.md) when the phase is completed. At this point, the preview interaction is complete, and you should update the UI appropriately. For example, in view controller preview interactions, the child view controller becomes the main view controller.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.
- `transitionProgress`: The progress through the commit phase of the transition. A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) with a value from `0` to `1`.
- `ended`: A `Boolean` whose value indicates whether the commit phase of the transition is complete.

## See Also

### Managing preview interactions
- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](./previewinteractionshouldbegin%28_%29.md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatepreviewtransition,ended%29.md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteractionDidCancel(UIPreviewInteraction)](./previewinteractiondidcancel%28_%29.md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:))*