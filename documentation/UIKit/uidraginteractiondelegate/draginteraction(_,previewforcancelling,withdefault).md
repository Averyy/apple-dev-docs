# dragInteraction(_:previewForCancelling:withDefault:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the targeted drag item preview to show during the cancellation animation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, previewForCancelling item: UIDragItem, withDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

```objc
- (UITargetedDragPreview *) dragInteraction:(UIDragInteraction *) interaction previewForCancellingItem:(UIDragItem *) item withDefault:(UITargetedDragPreview *) defaultPreview;
```

#### Return Value

- The default preview provided by the system.
- A targeted drag item preview you create.
- The preview returned after moving to a new preview target (using the `defaultPreview`’s [`retargetedPreview(with:)`](../uitargeteddragpreview/retargetedpreview%28with%29.md) method).
- `nil` to fade the preview that is currently displayed to the user, which is the same behavior as not implementing this method.

#### Discussion

The system calls this method multiple times, once for each visible drag item.

When you return a preview, the system shows it during the cancellation animation in order to visually “move” the drag item to the location of the preview’s associated `view`.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The drag item represented by the preview.
- `defaultPreview`: A targeted drag preview provided by the system.

## See Also

### Providing drag previews
- [func dragInteraction(UIDragInteraction, previewForLifting: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?](./draginteraction%28_,previewforlifting,session%29.md)
  Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [func dragInteraction(UIDragInteraction, prefersFullSizePreviewsFor: any UIDragSession) -> Bool](./draginteraction%28_,prefersfullsizepreviewsfor%29.md)
  Asks the delegate whether the preview should appear in its original size or a scaled size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforcancelling:withdefault:))*