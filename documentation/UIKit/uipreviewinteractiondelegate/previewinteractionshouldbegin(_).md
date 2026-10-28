# previewInteractionShouldBegin(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether a preview interaction is allowed to begin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewInteractionShouldBegin(_ previewInteraction: UIPreviewInteraction) -> Bool
```

```objc
- (BOOL) previewInteractionShouldBegin:(UIPreviewInteraction *) previewInteraction;
```

## Return Value

[`true`](../../Swift/true.md) if the preview interaction should continue into the preview and commit phases; otherwise [`false`](../../Swift/false.md).

## Discussion

If you don’t implement this optional method, the default return value of [`true`](../../Swift/true.md) is assumed.

When [`false`](../../Swift/false.md), no further delegate calls are made for the specified preview interaction until the user restarts the 3D Touch interaction.

## Parameters

- `previewInteraction`: The preview interaction that’s responding to user input.

## See Also

### Managing preview interactions
- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatepreviewtransition,ended%29.md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](./previewinteraction%28_,didupdatecommittransition,ended%29.md)
  Informs the delegate of the preview interaction’s progress through the commit phase.
- [func previewInteractionDidCancel(UIPreviewInteraction)](./previewinteractiondidcancel%28_%29.md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractionshouldbegin(_:))*