# UIDropInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for configuring and controlling a drop interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDropInteractionDelegate : NSObjectProtocol
```

```objc
@protocol UIDropInteractionDelegate <NSObject>
```

## Mentions

- [Making a view into a drop destination](./making-a-view-into-a-drop-destination.md)
- [Understanding a drag item as a promise](./understanding-a-drag-item-as-a-promise.md)

## Topics

### Handling the drop
- [func dropInteraction(UIDropInteraction, canHandle: any UIDropSession) -> Bool](./uidropinteractiondelegate/dropinteraction%28_,canhandle%29.md)
  Asks the delegate whether it can handle the session’s drag items.
- [func dropInteraction(UIDropInteraction, performDrop: any UIDropSession)](./uidropinteractiondelegate/dropinteraction%28_,performdrop%29.md)
  Tells the delegate it can request the item provider data from the session’s drag items.
### Tracking the drop movements
- [func dropInteraction(UIDropInteraction, sessionDidEnter: any UIDropSession)](./uidropinteractiondelegate/dropinteraction%28_,sessiondidenter%29.md)
  Tells the delegate the drop session has moved into the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidUpdate: any UIDropSession) -> UIDropProposal](./uidropinteractiondelegate/dropinteraction%28_,sessiondidupdate%29.md)
  Tells the delegate the drop session has changed.
- [func dropInteraction(UIDropInteraction, sessionDidExit: any UIDropSession)](./uidropinteractiondelegate/dropinteraction%28_,sessiondidexit%29.md)
  Tells the delegate the drop session has moved out of the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidEnd: any UIDropSession)](./uidropinteractiondelegate/dropinteraction%28_,sessiondidend%29.md)
  Tells the delegate the drop session has ended.
### Animating the drop
- [func dropInteraction(UIDropInteraction, item: UIDragItem, willAnimateDropWith: any UIDragAnimating)](./uidropinteractiondelegate/dropinteraction%28_,item,willanimatedropwith%29.md)
  Tells the delegate the system’s drop animation is about to start.
- [func dropInteraction(UIDropInteraction, previewForDropping: UIDragItem, withDefault: UITargetedDragPreview) -> UITargetedDragPreview?](./uidropinteractiondelegate/dropinteraction%28_,previewfordropping,withdefault%29.md)
  Asks the delegate for the targeted drag item preview to show during the drop animation.
- [func dropInteraction(UIDropInteraction, concludeDrop: any UIDropSession)](./uidropinteractiondelegate/dropinteraction%28_,concludedrop%29.md)
  Tells the delegate the drop activity and its related animations have finished.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Drag and drop interactions
- [protocol UIDragInteractionDelegate](./uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.
- [class UIDragInteraction](./uidraginteraction.md)
  An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.
- [class UIDropInteraction](./uidropinteraction.md)
  An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate)*