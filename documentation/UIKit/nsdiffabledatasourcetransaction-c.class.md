# NSDiffableDataSourceTransaction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A transaction that describes the changes after reordering the items in the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface NSDiffableDataSourceTransaction : NSObject
```

## Topics

### Accessing a transaction’s information
- [sectionTransactions](./nsdiffabledatasourcetransaction-c.class/sectiontransactions.md)
  An array of section transactions for the transaction.
- [initialSnapshot](./nsdiffabledatasourcetransaction-c.class/initialsnapshot.md)
  The snapshot before the transaction occured.
- [finalSnapshot](./nsdiffabledatasourcetransaction-c.class/finalsnapshot.md)
  The snapshot after the transaction occured.
- [difference](./nsdiffabledatasourcetransaction-c.class/difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Supporting reordering
- [var reorderingHandlers: __UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereference/reorderinghandlers.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereorderinghandlers.md)
  Handlers for reordering items.
- [NSDiffableDataSourceSectionTransaction](./nsdiffabledatasourcesectiontransaction-c.class.md)
  A transaction that describes the changes after reordering the items in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-c.class)*