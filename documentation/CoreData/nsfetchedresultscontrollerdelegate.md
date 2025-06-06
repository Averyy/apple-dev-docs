# NSFetchedResultsControllerDelegate

**Framework**: Core Data  
**Kind**: protocol

A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol NSFetchedResultsControllerDelegate : NSObjectProtocol
```

#### Overview

Consider whether to update the table view for each change. For a large number of simultaneous modifications simultaneously, such as if your app reads data on a background thread, it may be computationally expensive to animate all the changes. Rather than respond to changes individually (as illustrated in [`Typical use`](nsfetchedresultscontrollerdelegate#Typical-use.md)), implement [`controllerDidChangeContent(_:)`](nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:).md) to reload the table view after the system processes all pending changes.

> **Note**:  The fetched results controller reports changes to its section before changes to the fetched objects themselves.

 The fetched results controller reports changes to its section before changes to the fetched objects themselves.

##### Typical Use

When a fetched results controller provides the content to a table view, you can use [`controllerWillChangeContent(_:)`](nsfetchedresultscontrollerdelegate/controllerwillchangecontent(_:).md) and [`controllerDidChangeContent(_:)`](nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:).md) to bracket updates to the table view, as shown in the following example:

```swift
// Find out when the fetched results controller is about to start making changes.
func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    // Start animating table view changes simultaneously.
    tableView.beginUpdates()
}

// Find out when the fetched results controller finishes making changes.
func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    // Stop animating table view changes simultaneously.
    tableView.endUpdates()
}

// Find out when the fetched results controller adds or removes a section.
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange sectionInfo: NSFetchedResultsSectionInfo,
                atSectionIndex sectionIndex: Int,
                for type: NSFetchedResultsChangeType) {
    switch type {
    case .insert:
        // Insert a new section with fade animation.
        tableView.insertSections(IndexSet(integer: sectionIndex), with: .fade)
    case .delete:
        // Delete a section with fade animation.
        tableView.deleteSections(IndexSet(integer: sectionIndex), with: .fade)
    default:
        break
    }
}

// Find out when the fetched results controller adds, removes, moves, or
// updates a fetched object.
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange anObject: Any,
                at indexPath: IndexPath?,
                for type: NSFetchedResultsChangeType,
                newIndexPath: IndexPath?) {
    switch type {
    case .insert:
        guard let newIndexPath else { return }
        // Insert a new row with fade animation when the fetched results
        // controller adds or moves an object to the specified index path.
        tableView.insertRows(at: [newIndexPath], with: .fade)
    case .delete:
        guard let indexPath else { return }
        // Delete the row with animation at the old index path when the fetched
        // results controller deletes or moves the associated object.
        tableView.deleteRows(at: [indexPath], with: .fade)
    case .update:
        guard let indexPath else { return }
        // Update the cell as the specified indexPath.
        if let cell = tableView.cellForRow(at: indexPath) {
            cell.textLabel?.text = fetchedResultsController?.object(at: indexPath).name
        }
    case .move:
        guard let indexPath, let newIndexPath else { return }
        // Move a row from the specified index path to the new index path.
        tableView.moveRow(at: indexPath, to: newIndexPath)
    @unknown default:
        break
    }
}
```

##### User Driven Updates

In general, [`NSFetchedResultsControllerDelegate`](nsfetchedresultscontrollerdelegate.md) responds to changes at the model layer. If you allow a user to reorder table rows, then your implementation of the delegate methods needs to take this into account.

Typically, if you allow the user to reorder table rows, your model object has an attribute that specifies its index. When the user moves a row, you update this attribute accordingly. This, however, has the side effect of causing the fetched results controller to also notice the change, which causes it to inform its delegate of the update (using [`controller(_:didChange:at:for:newIndexPath:)`](nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:).md)). If you use the implementation of this method shown in the section above, then the delegate attempts to update the table view. However, the table view is already in the appropriate state because of the user’s action.

Therefore, if you support user-driven updates, you should check if the user intitiated a move, such as by setting a flag. In the implementation of your delegate methods, bypass the method implementation if the user initiated the move, for example:

```objc
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange anObject: Any,
                at indexPath: IndexPath?,
                for type: NSFetchedResultsChangeType,
                newIndexPath: IndexPath?) {
    // If you allow users to reorder table rows, bypass automated handling
    // of the change because the model layer already handles it.
    guard changeIsUserDriven == false else { return }
    
    switch type {
    case .insert:
        guard let newIndexPath else { return }
    // Remaining implementation.
}
```

> **Note**:  Prior to iOS 4.0, [`NSFetchedResultsController`](nsfetchedresultscontroller.md) doesn’t support deleting sections as a result of a UI-driven change.

 Prior to iOS 4.0, [`NSFetchedResultsController`](nsfetchedresultscontroller.md) doesn’t support deleting sections as a result of a UI-driven change.

## Topics

### Responding to Changes
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: CollectionDifference<NSManagedObjectID>)](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [func controllerWillChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](nsfetchedresultscontrollerdelegate/controllerwillchangecontent(_:).md)
  Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:).md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:).md)
  Notifies the receiver of the addition or removal of a section.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:).md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.
### Customizing Section Names
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, sectionIndexTitleForSectionName: String) -> String?](nsfetchedresultscontrollerdelegate/controller(_:sectionindextitleforsectionname:).md)
  Returns the name for a given section.
### Constants
- [enum NSFetchedResultsChangeType](nsfetchedresultschangetype.md)
  Constants that specify the possible types of changes that are reported.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFetchedResultsSectionInfo](nsfetchedresultssectioninfo.md)
  A protocol that defines the interface for section objects vended by a fetched results controller.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.
- [enum NSFetchedResultsChangeType](nsfetchedresultschangetype.md)
  Constants that specify the possible types of changes that are reported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate)*