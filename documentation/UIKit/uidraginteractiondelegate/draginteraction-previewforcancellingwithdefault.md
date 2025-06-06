# dragInteraction(_:previewForCancelling:withDefault:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the targeted drag item preview to show during the cancellation animation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, previewForCancelling item: UIDragItem, withDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

#### Return Value

- The default preview provided by the system.
- A targeted drag item preview you create.
- The preview returned after moving to a new preview target (using the `defaultPreview`’s [`retargetedPreview(with:)`](uitargeteddragpreview/retargetedpreview(with:).md) method).
- `nil` to fade the preview that is currently displayed to the user, which is the same behavior as not implementing this method.

#### Discussion

The system calls this method multiple times, once for each visible drag item.

When you return a preview, the system shows it during the cancellation animation in order to visually “move” the drag item to the location of the preview’s associated `view`.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The drag item represented by the preview.
- `defaultPreview`: A targeted drag preview provided by the system.

## See Also

- [func dragInteraction(UIDragInteraction, previewForLifting: UIDragItem, session: any UIDragSession) -> UITargetedDragPreview?](uidraginteractiondelegate/draginteraction(_:previewforlifting:session:).md)
  Asks the delegate for the targeted drag item preview that will appear during the lift animation.
- [func dragInteraction(UIDragInteraction, prefersFullSizePreviewsFor: any UIDragSession) -> Bool](uidraginteractiondelegate/draginteraction(_:prefersfullsizepreviewsfor:).md)
  Asks the delegate whether the preview should appear in its original size or a scaled size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:previewforcancelling:withdefault:))*