# controllerWillChangeContent(_:)

**Framework**: Core Data  
**Kind**: method

Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func controllerWillChangeContent(_ controller: NSFetchedResultsController<any NSFetchRequestResult>)
```

#### Discussion

This method is invoked before all invocations of [`controller(_:didChange:at:for:newIndexPath:)`](nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:).md) and [`controller(_:didChange:atSectionIndex:for:)`](nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:).md) have been sent for a given change event (such as the controller receiving a [`NSManagedObjectContextDidSave`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextDidSave) notification).

## Parameters

- `controller`: The fetched results controller that sent the message.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: CollectionDifference<NSManagedObjectID>)](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:).md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:).md)
  Notifies the receiver of the addition or removal of a section.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:).md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controllerwillchangecontent(_:))*