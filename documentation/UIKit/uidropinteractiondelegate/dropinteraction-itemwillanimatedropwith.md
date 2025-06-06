# dropInteraction(_:item:willAnimateDropWith:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the system’s drop animation is about to start.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, item: UIDragItem, willAnimateDropWith animator: any UIDragAnimating)
```

#### Discussion

This method is called for each drag item in the session, whether the item’s visible or not.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The current drag item.
- `animator`: The animator that provides custom animations to run alongside the system’s drop animation. You can also use it to add a completion block that runs after the animations have finished.

## See Also

- [func dropInteraction(UIDropInteraction, previewForDropping: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:).md)
  Asks the delegate for the targeted drag item preview to show during the drop animation.
- [func dropInteraction(UIDropInteraction, concludeDrop: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:concludedrop:).md)
  Tells the delegate the drop activity and its related animations have finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:item:willanimatedropwith:))*