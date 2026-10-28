# controllerWillChangeContent(_:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func controllerWillChangeContent(_ controller: NSFetchedResultsController<any NSFetchRequestResult>)
```

```objc
- (void) controllerWillChangeContent:(NSFetchedResultsController *) controller;
```

## Discussion

This method is invoked before all invocations of [`controller(_:didChange:at:for:newIndexPath:)`](./controller%28_,didchange,at,for,newindexpath%29.md) and [`controller(_:didChange:atSectionIndex:for:)`](./controller%28_,didchange,atsectionindex,for%29.md) have been sent for a given change event (such as the controller receiving a [`NSManagedObjectContextDidSave`](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) notification).

## Parameters

- `controller`: The fetched results controller that sent the message.

## See Also

### Related Documentation
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
### Responding to Changes
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](./controller%28_,didchangecontentwith%29-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: CollectionDifference<NSManagedObjectID>)](./controller%28_,didchangecontentwith%29-5ullb.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](./controller%28_,didchange,at,for,newindexpath%29.md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](./controller%28_,didchange,atsectionindex,for%29.md)
  Notifies the receiver of the addition or removal of a section.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](./controllerdidchangecontent%28_%29.md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controllerwillchangecontent(_:))*