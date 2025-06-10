# Making a view into a drag source

**Framework**: UIKit

Adopt drag interaction APIs to provide items for dragging.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

#### Overview

By implementing a drag interaction delegate ([`UIDragInteractionDelegate`](uidraginteractiondelegate.md)) for a view, you enable that view to function as a drag source in your app.

> **Note**:  The [`UITextView`](uitextview.md), [`UITableView`](uitableview.md), and [`UICollectionView`](uicollectionview.md) classes each provide their own, specialized support for creating drag items. See these classes for more information.

##### Enable a View As a Drag Source

Any instance or subclass of [`UIView`](uiview.md) can act as a drag source. Your first steps to make this happen are:

1. Create a drag interaction (a [`UIDragInteraction`](uidraginteraction.md) instance).
2. Specify the drag interaction’s delegate (an object that conforms to the [`UIDragInteractionDelegate`](uidraginteractiondelegate.md) protocol).
3. Add the interaction to the view’s [`interactions`](uiview/interactions.md) property.

Here’s how to do this using a custom helper method, which you’d typically call within a view controller’s [`viewDidLoad()`](uiviewcontroller/viewdidload().md) method:

```swift
func customEnableDragging(on view: UIView, dragInteractionDelegate: UIDragInteractionDelegate) {
    let dragInteraction = UIDragInteraction(delegate: dragInteractionDelegate)
    view.addInteraction(dragInteraction)
}
```

##### Create a Drag Item

A drag item encapsulates a source app’s promises for providing a variety of data representations for one model object.

To create a drag item, implement the [`dragInteraction(_:itemsForBeginning:)`](uidraginteractiondelegate/draginteraction(_:itemsforbeginning:).md) method in your drag interaction delegate, as shown here in a minimal form:

```swift
func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: UIDragSession) -> [UIDragItem] {
    // Cast to NSString is required for NSItemProviderWriting support.
    let stringItemProvider = NSItemProvider(object: "Hello World" as NSString)
    return [
        UIDragItem(itemProvider: stringItemProvider)
    ]
}
```

> **Note**:  The cast from the Swift [`String`](https://developer.apple.com/documentation/Swift/String) type to the Foundation [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) class, in the code snippet above, is required because model objects for drag and drop must support the [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting) protocol.

This implementation uses the [`init(object:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/init(object:)) convenience initializer. When you instantiate a drag item, pass an object in your app’s native representation, or in the highest-fidelity representation you support. In general, ensure that the first element in the item provider’s [`registeredTypeIdentifiers`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registeredTypeIdentifiers) array represents the highest-fidelity data your drag interaction delegate can deliver.

To add more data representations to a drag item, as you typically would in your app, add them in fidelity order, from highest to lowest. When adding representations, you have choices:

- The best option for adding multiple data representations to a drag item, in many cases, is to adopt the [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting) protocol in your model class. Using this protocol, you place the code for providing multiple data representations within the model class.
- You can use the [`registerObject(_:visibility:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registerObject(_:visibility:)) method, or related methods, from the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) class, to explicitly register data representations.

##### Understand a Drag Source in Context

In the [`dragInteraction(_:itemsForBeginning:)`](uidraginteractiondelegate/draginteraction(_:itemsforbeginning:).md) protocol method, your source app responds to a request from the system. This request is itself triggered by the user starting to drag an item in your app’s UI. The conversation between your app and the system proceeds as shown here:

![APIs for providing drag items from a drag source](https://docs-assets.developer.apple.com/published/ef04a983c2d83148c7e1929bce5ea101/media-2903752%402x.png)

The figure above depicts the steps for constructing a drag item, in context:

1. The user initiates a drag activity with a long press on a view in your app, followed by moving their finger while still touching the screen. The system instantiates a drag session (an object that conforms to the [`UIDragSession`](uidragsession.md) protocol, not shown in the figure) for managing the drag activity.
2. The system calls the drag interaction delegate’s [`dragInteraction(_:itemsForBeginning:)`](uidraginteractiondelegate/draginteraction(_:itemsforbeginning:).md) protocol method. Your delegate returns one or more drag items.
3. Finally, the system populates the drag session with your drag items, ready for the user to move the drag session to a destination.

## See Also

- [Understanding a drag item as a promise](understanding-a-drag-item-as-a-promise.md)
  Use drag items to convey data representation promises between a source app and a destination app.
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
  Adopt drop interaction APIs to selectively consume dragged content.
- [Adopting drag and drop in a custom view](adopting-drag-and-drop-in-a-custom-view.md)
  Demonstrates how to enable drag and drop for a `UIImageView` instance.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/making-a-view-into-a-drag-source)*