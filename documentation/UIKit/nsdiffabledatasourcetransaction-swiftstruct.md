# NSDiffableDataSourceTransaction

**Framework**: UIKit  
**Kind**: struct

A transaction that describes the changes after reordering the items in the view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
struct NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Topics

### Accessing a transaction’s information
- [var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>]](nsdiffabledatasourcetransaction-swift.struct/sectiontransactions.md)
  An array of section transactions for the transaction.
- [var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/initialsnapshot.md)
  The snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/finalsnapshot.md)
  The snapshot after the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSource.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md)
  Handlers for reordering items.
- [struct NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct)*