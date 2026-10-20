# previewInteraction(_:didUpdatePreviewTransition:ended:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the delegate of the progress through the preview phase of the preview interaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func previewInteraction(_ previewInteraction: UIPreviewInteraction, didUpdatePreviewTransition transitionProgress: CGFloat, ended: Bool)
```

```objc
- (void) previewInteraction:(UIPreviewInteraction *) previewInteraction didUpdatePreviewTransition:(CGFloat) transitionProgress ended:(BOOL) ended;
```

#### Discussion

This method is called repeatedly during the preview phase of the preview interaction. Use the supplied `transitionProgress` parameter to update the UI to reflect the progress of the interaction. For example, the *peek* effect in view controller preview transitions progressively blurs everything except the appropriate view.

The `ended` parameter is [`false`](../../Swift/false.md) throughout the preview phase and becomes [`true`](../../Swift/true.md) as the phase is completed. The preview interaction then transitions to the commit phase, so you should use this point to update the UI as required.

## Parameters

- `previewInteraction`: The preview interaction associated with the current user input.
- `transitionProgress`: The progress through the preview phase of the transition. A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) with a value from `0` to `1`.
- `ended`: A Boolean whose value indicates whether the preview phase of the transition is complete.

## See Also

### Managing preview interactions
- [func previewInteractionShouldBegin(UIPreviewInteraction) -> Bool](./previewinteractionshouldbegin%28_%29.md)
  Asks the delegate whether a preview interaction is allowed to begin.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatecommittransition,ended%29.md)
  Informs the delegate of the preview interaction’s progress through the commit phase.
- [func previewInteractionDidCancel(UIPreviewInteraction)](./previewinteractiondidcancel%28_%29.md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:))*