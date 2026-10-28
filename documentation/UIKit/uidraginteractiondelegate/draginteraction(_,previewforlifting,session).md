# dragInteraction(_:previewForLifting:session:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the targeted drag item preview that will appear during the lift animation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, previewForLifting item: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?
```

```objc
- (UITargetedDragPreview *) dragInteraction:(UIDragInteraction *) interaction previewForLiftingItem:(UIDragItem *) item session:(id<UIDragSession>) session;
```

## Return Value

A targeted drag item preview you create, or `nil` to tell the system not to display the lift animation.

## Discussion

If you don’t provide this method, the system creates a preview based on the view owned by the drag interaction.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The drag item represented by the preview.
- `session`: The current drag session.

## See Also

### Providing drag previews
- [func dragInteraction(UIDragInteraction, previewForCancelling: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](./draginteraction%28_,previewforcancelling,withdefault%29.md)
  Asks the delegate for the targeted drag item preview to show during the cancellation animation.
- [func dragInteraction(UIDragInteraction, prefersFullSizePreviewsFor: any UIDragSession) -> Bool](./draginteraction%28_,prefersfullsizepreviewsfor%29.md)
  Asks the delegate whether the preview should appear in its original size or a scaled size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforlifting:session:))*