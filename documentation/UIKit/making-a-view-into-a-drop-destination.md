# Making a view into a drop destination

**Framework**: UIKit

Adopt drop interaction APIs to selectively consume dragged content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

#### Overview

By implementing a drop interaction delegate ([`UIDropInteractionDelegate`](uidropinteractiondelegate.md)) for a view, you enable that view to accept dropped items.

> **Note**:  The [`UITextView`](uitextview.md), [`UITableView`](uitableview.md), and [`UICollectionView`](uicollectionview.md) classes each provide their own, specialized support for consuming drag items. See these classes for more information.

##### Enable a View As a Drop Destination

Any instance or subclass of [`UIView`](uiview.md) can act as a drop destination. Your first steps to make this happen are:

1. Create a drop interaction (a [`UIDropInteraction`](uidropinteraction.md) instance).
2. Specify the drop interaction’s delegate (an object that conforms to the [`UIDropInteractionDelegate`](uidropinteractiondelegate.md) protocol).
3. Add the interaction to the view’s [`interactions`](uiview/interactions.md) property.

Here’s how to do this:

```swift
func customEnableDropping(on view: UIView, dropInteractionDelegate: UIDropInteractionDelegate) {
    let dropInteraction = UIDropInteraction(delegate: dropInteractionDelegate)
    view.addInteraction(dropInteraction)
}
```

##### Consider Accepting the Drag Items

When the user moves the touch point of a drag session over a drop destination, you can immediately refuse it, or you can tell the system to continue its conversation with your delegate object. Provide your response as follows:

```swift
func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    // Ensure the drop session has an object of the appropriate type
    return session.canLoadObjects(ofClass: UIImage.self)
}
```

This example assumes that your drop destination can consume only [`UIImage`](uiimage.md) objects. The method implementation tests for this type in the `return` statement. You can also use this method to refuse a drop session based on the state of your app. The  is a system-managed object that conforms to the [`UIDropSession`](uidropsession.md) protocol. You can access a drop session for information about the items being dropped.

The [`dropInteraction(_:canHandle:)`](uidropinteractiondelegate/dropinteraction(_:canhandle:).md) method is your app’s only chance to respond to the system’s question about whether your app will  accepting the items. For example, you might preemptively reject a drop session if it contains no data representations your app can consume, or if consuming dragged items is inappropriate given your app state. Your app’s definitive opportunity to accept or reject dropped items is in your implementation of the [`dropInteraction(_:sessionDidUpdate:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md) protocol method.

##### Provide the Required Drop Proposal

For a view to be eligible to accept the data from a drop session, you  implement the [`dropInteraction(_:sessionDidUpdate:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md) protocol method. In your implementation, return a drop proposal—a [`UIDropProposal`](uidropproposal.md) object that specifies the drop operation type, a constant from the [`UIDropOperation`](uidropoperation.md) enumeration.

Provide a drop proposal like this:

```swift
func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: UIDropSession) -> UIDropProposal {
        // Propose to the system to copy the item from the source app
        return UIDropProposal(operation: .copy)
}

```

If your app instead opts to refuse the dropped items, return the [`UIDropOperation.cancel`](uidropoperation/cancel.md) constant.

The system calls this protocol method when the user has moved the touch point of a drag session over a drop-enabled view — as long as the view didn’t already reject the drop by returning `false` in its [`dropInteraction(_:canHandle:)`](uidropinteractiondelegate/dropinteraction(_:canhandle:).md) method (see [`Consider accepting the drag items`](making-a-view-into-a-drop-destination#Consider-accepting-the-drag-items.md)).

##### Consume the Data in the Drag Items

The final step of the conversation between the drop interaction delegate and the system is when your app consumes the data the user has dragged from the source app. Here, your drop interaction delegate asks the drop session to load its drag items:

```swift
func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
    // Consume drag items (in this example, of type UIImage).
    session.loadObjects(ofClass: UIImage.self) { imageItems in
        let images = imageItems as! [UIImage]
        self.imageView.image = images.first
    }
    // Perform additional UI updates as needed.
}
```

The [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) method is a destination app’s only opportunity to request representations of drag items. Receiving the items is potentially time-consuming and proceeds asynchronously.  wait within this method to receive items; instead, return from this method quickly.

> **Note**:  If you don’t employ the [`loadObjects(ofClass:completion:)`](uidropsession/loadobjects(ofclass:completion:).md) convenience method as shown above, which automatically employs the main thread, explicitly dispatch UI work to the main thread. For example, you can use the `DispatchQueue.main.async` function.

##### Understand a Drop Destination in Context

When the touch point for a drop session moves over a view that you’ve configured as a drop destination, the system initiates a conversation with the drop interaction delegate. This conversation gives your app opportunities to accept or reject the drop, to prepare for consuming the drag items, and to update your model and UI, as shown here:

![APIs for consuming data from drag items in a drop destination](https://docs-assets.developer.apple.com/published/67b275f6dcc278f02bdbad17ff2c6a7e/media-2903753%402x.png)

The figure above depicts the steps for consuming a drag item, in context:

1. The user moves their finger onscreen so the touch point of a drag session is within a configured view in your app. The system instantiates a drop session (an object that conforms to the [`UIDropSession`](uidropsession.md) protocol, not shown in the figure) for managing the drop activity.
2. The system calls the drop interaction delegate’s [`dropInteraction(_:canHandle:)`](uidropinteractiondelegate/dropinteraction(_:canhandle:).md) protocol method. Check whether your app can, and opts to, consume the drag items.
3. The system calls the delegate’s [`dropInteraction(_:sessionDidEnter:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidenter:).md) protocol method. Prepare to consume the drag items.
4. The system calls the delegate’s [`dropInteraction(_:sessionDidUpdate:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md) protocol method. Your implementation  return a [`UIDropProposal`](uidropproposal.md) object, or the system ends the session.
5. If the user confirms their intent to complete the drop, the system calls the delegate’s asynchronous [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) protocol method. This a destination app’s only opportunity to request representations of drag items.

## See Also

- [Understanding a drag item as a promise](understanding-a-drag-item-as-a-promise.md)
  Use drag items to convey data representation promises between a source app and a destination app.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt drag interaction APIs to provide items for dragging.
- [Adopting drag and drop in a custom view](adopting-drag-and-drop-in-a-custom-view.md)
  Demonstrates how to enable drag and drop for a `UIImageView` instance.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/making-a-view-into-a-drop-destination)*