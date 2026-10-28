# dragInteraction(_:prefersFullSizePreviewsFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the preview should appear in its original size or a scaled size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, prefersFullSizePreviewsFor session: any UIDragSession) -> Bool
```

```objc
- (BOOL) dragInteraction:(UIDragInteraction *) interaction prefersFullSizePreviewsForSession:(id<UIDragSession>) session;
```

## Return Value

[`true`](../../Swift/true.md) to tell the system the preview should appear in its original size; otherwise [`false`](../../Swift/false.md), which is the default if you don’t provide this method.

## Discussion

The return value is a recommendation to the system. The system may choose to scale the preview to a smaller size, according to its own rules, even if you return [`true`](../../Swift/true.md).

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drag session.

## See Also

### Providing drag previews
- [func dragInteraction(UIDragInteraction, previewForLifting: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?](./draginteraction%28_,previewforlifting,session%29.md)
  Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [func dragInteraction(UIDragInteraction, previewForCancelling: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](./draginteraction%28_,previewforcancelling,withdefault%29.md)
  Asks the delegate for the targeted drag item preview to show during the cancellation animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:prefersfullsizepreviewsfor:))*