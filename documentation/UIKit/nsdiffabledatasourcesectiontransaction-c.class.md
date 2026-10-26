# NSDiffableDataSourceSectionTransaction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A transaction that describes the changes after reordering the items in a section.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface NSDiffableDataSourceSectionTransaction : NSObject
```

## Topics

### Accessing a transaction’s information
- [sectionIdentifier](./nsdiffabledatasourcesectiontransaction-c.class/sectionidentifier.md)
  The identifier of the section for the transaction.
- [initialSnapshot](./nsdiffabledatasourcesectiontransaction-c.class/initialsnapshot.md)
  The section snapshot before the transaction occured.
- [finalSnapshot](./nsdiffabledatasourcesectiontransaction-c.class/finalsnapshot.md)
  The section snapshot after the transaction occured.
- [difference](./nsdiffabledatasourcesectiontransaction-c.class/difference.md)
  A collection of insertions and removals that describe the difference between initial and final section snapshots.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Supporting reordering
- [var reorderingHandlers: __UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereference/reorderinghandlers.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereorderinghandlers.md)
  Handlers for reordering items.
- [NSDiffableDataSourceTransaction](./nsdiffabledatasourcetransaction-c.class.md)
  A transaction that describes the changes after reordering the items in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class)*