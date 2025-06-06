# dropInteraction(_:concludeDrop:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the drop activity and its related animations have finished.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, concludeDrop session: any UIDropSession)
```

#### Discussion

When the interaction calls this method, update the interaction’s view with its post-drop appearance.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drop session that has finished.

## See Also

- [func dropInteraction(UIDropInteraction, item: UIDragItem, willAnimateDropWith: any UIDragAnimating)](uidropinteractiondelegate/dropinteraction(_:item:willanimatedropwith:).md)
  Tells the delegate the system’s drop animation is about to start.
- [func dropInteraction(UIDropInteraction, previewForDropping: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:).md)
  Asks the delegate for the targeted drag item preview to show during the drop animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:concludedrop:))*