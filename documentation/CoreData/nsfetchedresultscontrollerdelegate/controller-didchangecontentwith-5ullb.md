# controller(_:didChangeContentWith:)

**Framework**: Core Data  
**Kind**: method

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

#### Discussion

This method is only invoked if the controller’s [`sectionNameKeyPath`](nsfetchedresultscontroller/sectionnamekeypath.md) property is `nil` and [`controller(_:didChangeContentWith:)`](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq.md) is not implemented.

If this method is implemented, no other delegate methods are invoked.

## See Also

- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controllerWillChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](nsfetchedresultscontrollerdelegate/controllerwillchangecontent(_:).md)
  Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:).md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: any NSFetchedResultsSectionInfo, atSectionIndex: Int, for: NSFetchedResultsChangeType)](nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:).md)
  Notifies the receiver of the addition or removal of a section.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:).md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb)*