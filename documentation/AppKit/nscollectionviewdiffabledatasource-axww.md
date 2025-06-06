# NSCollectionViewDiffableDataSource

**Framework**: AppKit  
**Kind**: class

The object you use to manage data and provide items for a collection view.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
class NSCollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, ItemIdentifierType : Hashable
```

#### Overview

A  object is a specialized type of data source that works together with your collection view object. It provides the behavior you need to manage updates to your collection view’s data and UI in a simple, efficient way. It also conforms to the [`NSCollectionViewDataSource`](nscollectionviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a collection view with data:

1. Connect a diffable data source to your collection view.
2. Implement an item provider to configure your collection view’s items.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a collection view, you create the diffable data source using its [`init(collectionView:itemProvider:)`](nscollectionviewdiffabledatasource-axww/init(collectionview:itemprovider:).md) initializer, passing in the collection view you want to associate with that data source. You also pass in an item provider, where you configure each of your items to determine how to display your data in the UI.

```swift
dataSource = NSCollectionViewDiffableDataSource<Int, UUID>(collectionView: collectionView) {
    (collectionView: NSCollectionView, indexPath: IndexPath, itemIdentifier: UUID) -> NSCollectionViewItem? in
    // configure and return item
}
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md).

## Topics

### Creating a Diffable Data Source
- [init(collectionView: NSCollectionView, itemProvider: NSCollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ItemProvider)](nscollectionviewdiffabledatasource-axww/init(collectionview:itemprovider:).md)
  Creates a diffable data source with the specified item provider, and connects it to the specified collection view.
- [NSCollectionViewDiffableDataSource.ItemProvider](nscollectionviewdiffabledatasource-axww/itemprovider.md)
  A closure that configures and returns an item for a collection view from its diffable data source.
### Creating Supplementary Views
- [var supplementaryViewProvider: NSCollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SupplementaryViewProvider?](nscollectionviewdiffabledatasource-axww/supplementaryviewprovider-swift.property.md)
  The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.
- [NSCollectionViewDiffableDataSource.SupplementaryViewProvider](nscollectionviewdiffabledatasource-axww/supplementaryviewprovider-swift.typealias.md)
  A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.
### Identifying Items
- [func itemIdentifier(for: IndexPath) -> ItemIdentifierType?](nscollectionviewdiffabledatasource-axww/itemidentifier(for:).md)
  Returns an identifier for the item at the specified index path in the collection view.
- [func indexPath(for: ItemIdentifierType) -> IndexPath?](nscollectionviewdiffabledatasource-axww/indexpath(for:).md)
  Returns an index path for the item with the specified identifier in the collection view.
### Updating Data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nscollectionviewdiffabledatasource-axww/snapshot.md)
  Returns a representation of the current state of the data in the collection view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](nscollectionviewdiffabledatasource-axww/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
### Supporting Protocol Requirements
- [Protocol Implementations](protocol-implementations.md)
  Access the diffable data source’s implementations of protocol methods.
### Instance Methods
- [func description() -> String](nscollectionviewdiffabledatasource-axww/description.md)
  Returns a string with a description of the diffable data source.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCollectionViewDataSource](nscollectionviewdatasource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSCollectionViewDataSource](nscollectionviewdatasource.md)
  A set of methods that a data source object implements to provide the information and view objects that a collection view requires to present content.
- [protocol NSCollectionViewDelegate](nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasource-axww)*