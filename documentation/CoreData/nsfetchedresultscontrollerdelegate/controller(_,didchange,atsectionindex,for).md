# controller(_:didChange:atSectionIndex:for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver of the addition or removal of a section.

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
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChange sectionInfo: any NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType)
```

```objc
- (void) controller:(NSFetchedResultsController *) controller didChangeSection:(id<NSFetchedResultsSectionInfo>) sectionInfo atIndex:(NSUInteger) sectionIndex forChangeType:(NSFetchedResultsChangeType) type;
```

## Discussion

The fetched results controller reports changes to its section before changes to the fetched result objects.

### Special Considerations

This method may be invoked many times during an update event (for example, if you are importing data on a background thread and adding them to the context in a batch). You should consider carefully whether you want to update the table view on receipt of each message.

## Parameters

- `controller`: The fetched results controller that sent the message.
- `sectionInfo`: The section that changed.
- `sectionIndex`: The index of the changed section.
- `type`: The type of change (insert or delete). Valid values are [`NSFetchedResultsChangeType.insert`](../nsfetchedresultschangetype/insert.md) and [`NSFetchedResultsChangeType.delete`](../nsfetchedresultschangetype/delete.md).

## See Also

### Responding to Changes
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: NSDiffableDataSourceSnapshot)](./controller%28_,didchangecontentwith%29-4kezq.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith: CollectionDifference<NSManagedObjectID>)](./controller%28_,didchangecontentwith%29-5ullb.md)
  Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [func controllerWillChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](./controllerwillchangecontent%28_%29.md)
  Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [func controller(NSFetchedResultsController<any NSFetchRequestResult>, didChange: Any, at: IndexPath?, for: NSFetchedResultsChangeType, newIndexPath: IndexPath?)](./controller%28_,didchange,at,for,newindexpath%29.md)
  Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [func controllerDidChangeContent(NSFetchedResultsController<any NSFetchRequestResult>)](./controllerdidchangecontent%28_%29.md)
  Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:))*