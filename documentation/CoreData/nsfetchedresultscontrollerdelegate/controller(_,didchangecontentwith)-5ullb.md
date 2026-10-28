# controller(_:didChangeContentWith:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith diff: CollectionDifference<NSManagedObjectID>)
```

```objc
- (void) controller:(NSFetchedResultsController *) controller didChangeContentWithDifference:(NSOrderedCollectionDifference<NSManagedObjectID *> *) diff;
```

## Discussion

This method is only invoked if the controller’s [`sectionNameKeyPath`](../nsfetchedresultscontroller/sectionnamekeypath.md) property is `nil` and [`controller(_:didChangeContentWith:)`](./controller%28_,didchangecontentwith%29-4kezq.md) is not implemented.

If this method is implemented, no other delegate methods are invoked.

## See Also

### Responding to Changes
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](./controller%28_,didchangecontentwith%29-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controllerWillChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](./controllerwillchangecontent%28_%29.md)
  Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](./controller%28_,didchange,at,for,newindexpath%29.md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](./controller%28_,didchange,atsectionindex,for%29.md)
  Notifies the receiver of the addition or removal of a section.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](./controllerdidchangecontent%28_%29.md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb)*