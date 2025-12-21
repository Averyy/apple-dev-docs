# previewInteractionShouldBegin(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether a preview interaction is allowed to begin.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func previewInteractionShouldBegin(_ previewInteraction: UIPreviewInteraction) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the preview interaction should continue into the preview and commit phases; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you don’t implement this optional method, the default return value of [`true`](https://developer.apple.com/documentation/Swift/true) is assumed.

When [`false`](https://developer.apple.com/documentation/Swift/false), no further delegate calls are made for the specified preview interaction until the user restarts the 3D Touch interaction.

## Parameters

- `previewInteraction`: The preview interaction that’s responding to user input.

## See Also

- [func previewInteraction(UIPreviewInteraction, didUpdatePreviewTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatepreviewtransition:ended:).md)
  Informs the delegate of the progress through the preview phase of the preview interaction.
- [func previewInteraction(UIPreviewInteraction, didUpdateCommitTransition: CGFloat, ended: Bool)](uipreviewinteractiondelegate/previewinteraction(_:didupdatecommittransition:ended:).md)
  Informs the delegate of the preview interaction’s progress through the commit phase.
- [func previewInteractionDidCancel(UIPreviewInteraction)](uipreviewinteractiondelegate/previewinteractiondidcancel(_:).md)
  Informs the delegate that the specified preview interaction was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteractiondelegate/previewinteractionshouldbegin(_:))*