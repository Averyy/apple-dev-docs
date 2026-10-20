# dropInteraction(_:previewForDropping:withDefault:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the targeted drag item preview to show during the drop animation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, previewForDropping item: UIDragItem, withDefault defaultPreview: UITargetedDragPreview) -> UITargetedDragPreview?
```

```objc
- (UITargetedDragPreview *) dropInteraction:(UIDropInteraction *) interaction previewForDroppingItem:(UIDragItem *) item withDefault:(UITargetedDragPreview *) defaultPreview;
```

#### Return Value

- The default preview, which is the same behavior as not implementing this method.
- A targeted drag item preview that you create.
- The preview returned after moving to a new preview target by using the `defaultPreview`’s [`retargetedPreview(with:)`](../uitargeteddragpreview/retargetedpreview%28with%29.md) method.
- `nil` to fade the preview that is currently displayed to the user.

#### Discussion

The system calls this method multiple times, once for each visible drag item. It shows the preview during the drop animation in order to visually *drop* the drag item into place.

If you call [`setNeedsDropPreviewUpdate()`](../uidragitem/setneedsdroppreviewupdate%28%29.md) to tell the system to request a new drop preview, the system provides the previous value in the `defaultPreview` parameter.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The drag item represented by the preview.
- `defaultPreview`: A targeted drag preview provided by the system, if this is the first call for this item; otherwise, it’s the previous value for the drag preview.

## See Also

### Animating the drop
- [func dropInteraction(UIDropInteraction, item: UIDragItem, willAnimateDropWith: any UIDragAnimating)](./dropinteraction%28_,item,willanimatedropwith%29.md)
  Tells the delegate the system’s drop animation is about to start.
- [func dropInteraction(UIDropInteraction, concludeDrop: any UIDropSession)](./dropinteraction%28_,concludedrop%29.md)
  Tells the delegate the drop activity and its related animations have finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:))*