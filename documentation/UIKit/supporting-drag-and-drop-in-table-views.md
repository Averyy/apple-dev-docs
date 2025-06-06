# Supporting drag and drop in table views

**Framework**: Uikit

Initiate drags and handle drops from a table view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

#### Overview

Table views support drag and drop through a specialized API that works with the rows being displayed. To support drags, define a drag delegate object (an object that adopts the [`UITableViewDragDelegate`](uitableviewdragdelegate.md) protocol) and assign it to the [`dragDelegate`](uitableview/dragdelegate.md) property of your table view. To handle drops, define a drop delegate object (an object that adopts the [`UITableViewDropDelegate`](uitableviewdropdelegate.md) protocol) and assign it to the [`dropDelegate`](uitableview/dropdelegate.md) property of your table view.

##### Dragging Rows From the Table View

The table view manages most drag-related interactions, but you need to specify which rows to drag. When the drag gesture occurs, the table view creates a drag session and calls the [`tableView(_:itemsForBeginning:at:)`](uitableviewdragdelegate/tableview(_:itemsforbeginning:at:).md) method of your drag delegate object. (When the user drags a selected row, this method is called once for each row in the selection. If no rows are selected, the method is called only once for the underlying row.) If you return a non empty array, the table view begins dragging the rows that you specify. Return an empty array when you don’t allow the user to drag content from the specified index path.

> **Note**:  Use the other methods of the [`UITableViewDragDelegate`](uitableviewdragdelegate.md) protocol to manage additional drag-related interactions. For example, you can customize the appearance of the rows being dragged and let the user add items to the current drag session.

In your implementation of the [`tableView(_:itemsForBeginning:at:)`](uitableviewdragdelegate/tableview(_:itemsforbeginning:at:).md) method, do the following:

1. Create one or more [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects. Use the item providers to represent the data for your table’s rows.
2. Wrap each item provider object in a [`UIDragItem`](uidragitem.md) object.
3. Consider assigning a value to the [`localObject`](uidragitem/localobject.md) property of each drag item. This step is optional but makes it faster to drag and drop content within the same app.
4. Return the drag items from your method.

Use the provided index path to determine the row for which to create a drag item. If the target row is one of the currently selected rows, the table view automatically drags all of the selected rows. If the row isn’t part of the current selection, the table view adds it to the already active drag operation.

For more information about initiating drags, see [`UITableViewDragDelegate`](uitableviewdragdelegate.md).

##### Receiving Dropped Content

When content is dragged inside its bounds, a table view consults its drop delegate to determine whether it can receive the dragged data. Initially, the table view calls only the [`tableView(_:canHandle:)`](uitableviewdropdelegate/tableview(_:canhandle:).md) method of the drop delegate to determine whether you can incorporate the specified data into your data source. If you can incorporate the data, the table view begins calling other methods to determine where the data can be dropped.

As the user’s finger moves, the table view tracks the potential drop location and notifies your delegate by calling its [`tableView(_:dropSessionDidUpdate:withDestinationIndexPath:)`](uitableviewdropdelegate/tableview(_:dropsessiondidupdate:withdestinationindexpath:).md) method for each change. Implementing this method is optional but recommended, because it lets the table view display visual feedback about how dragged content will be incorporated. In your implementation, create a [`UITableViewDropProposal`](uitableviewdropproposal.md) object with information about how you’d respond to a drop at the specified index path. For example, you might want to insert the content as a new row into your data source or you might add the data into the existing row at the specified index path. Because the method is called frequently, return your proposal as quickly as possible. If you don’t implement this method, the table view doesn’t provide visual feedback about how it handles the drop.

When the user commits the drop by lifting the associated finger from the screen, the table view calls the [`tableView(_:performDropWith:)`](uitableviewdropdelegate/tableview(_:performdropwith:).md) method of your drop delegate. You must implement this method to handle the dropped data. In your implementation, fetch the dragged data, update your table view’s data source, and insert any needed rows into the table view itself. If the content originated from the table view, you can delete the dragged rows from their current location and insert them at their new location using the existing table view APIs. For content that came from outside the table view, use the [`localObject`](uidragitem/localobject.md) property (for content that originated inside your app) or the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object to fetch the data and insert it.

In your implementation of the [`tableView(_:performDropWith:)`](uitableviewdropdelegate/tableview(_:performdropwith:).md) method, do the following:

1. Iterate over the `items` property in the provided drop coordinator object.
2. For each item, determine how you want to handle its content:

- If the `sourceIndexPath` of the item contains a value, the item originated in the table view. Use a batch update to delete the item from its current location and insert it at the new index path.
- If the [`localObject`](uidragitem/localobject.md) property of the drag item is set, the content originated from elsewhere in your app so you must insert a row or update an existing item.
- If no other option is available, use the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) in the drag item’s [`itemProvider`](uidragitem/itemprovider.md) property to fetch the data asynchronously and insert or update the item.

1. Update your data source and insert or move the necessary items in the table view.

For content that’s already local to your app, you can usually update your table view’s data source and interface directly. For example, you might use a batch update to delete and then insert rows that dragged within the table view. When finished, call the [`drop(_:toRowAt:)`](uitableviewdropcoordinator/drop(_:torowat:).md) method of the drop coordinator to animate the insertion of the dragged content into the table view.

For data that must be retrieved using an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object, insert a placeholder into the table view until you’re able to retrieve the actual data. Inserting a placeholder is necessary only when inserting new rows into the table view. The placeholder acts as a temporary row, presenting the default content you want to display until the actual data becomes available. For example, you might provide a placeholder row with a text field stating that the content is currently loading.

To insert a placeholder into the table view, do the following:

1. Call the `drop(_:toPlaceholderInsertedAt:withReuseIdentifier:rowHeight:cellUpdateHandler:)` method of the provided [`UITableViewDropCoordinator`](uitableviewdropcoordinator.md) object to insert your placeholder row into the table view. Use the block in the `cellUpdateHandler` parameter to configure the contents of your placeholder cell.
2. Begin loading the data asynchronously from the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object.

When the [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) object returns the actual data, commit the insertion and exchange the placeholder cell for the final cell. Specifically, call the [`commitInsertion(dataSourceUpdates:)`](uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md) method of the context object you received after creating the placeholder. In the block that you pass to that method, update your model object and your table view’s data source. When this method returns, the table view automatically deletes the placeholder and inserts the final row, which causes your updated data to be reflected in a new cellInsert placeholders at the location specified by the `destinationIndexPath` property of the drop coordinator.

## See Also

- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.
- [protocol UITableViewDragDelegate](uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [protocol UITableViewDropCoordinator](uitableviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the table view.
- [protocol UITableViewDropItem](uitableviewdropitem.md)
  The data associated with an item being dropped into the table view.
- [class UITableViewDropProposal](uitableviewdropproposal.md)
  Your proposed solution for handling a drop in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/supporting-drag-and-drop-in-table-views)*