# NSDiffableDataSourceSectionTransaction

**Framework**: UIKit  
**Kind**: struct

A transaction that describes the changes after reordering the items in a section.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
struct NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Topics

### Accessing a transaction’s information
- [var sectionIdentifier: SectionIdentifierType](nsdiffabledatasourcesectiontransaction-swift.struct/sectionidentifier.md)
  The identifier of the section for the transaction.
- [var initialSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot.md)
  The section snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot.md)
  The section snapshot after the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/difference.md)
  A collection of insertions and removals that describe the difference between initial and final section snapshots.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSource.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md)
  Handlers for reordering items.
- [struct NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct)*