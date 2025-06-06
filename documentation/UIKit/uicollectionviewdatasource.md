# UICollectionViewDataSource

**Framework**: UIKit  
**Kind**: protocol

The methods adopted by the object you use to manage data and provide cells for a collection view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UICollectionViewDataSource : NSObjectProtocol
```

#### Overview

A data source object manages the data in your collection view. It represents your app’s data model and vends information to the collection view as needed. It also creates and configures the cells and supplementary views that the collection view uses to display your data.

A collection view data source must conform to the [`UICollectionViewDataSource`](uicollectionviewdatasource.md) protocol. You can use a [`UICollectionViewDiffableDataSource`](uicollectionviewdiffabledatasource-9tqpa.md) object as your data source object, which already conforms to this protocol.

Alternatively, you can create a custom data source object by adopting the [`UICollectionViewDataSource`](uicollectionviewdatasource.md) protocol. At a minimum, all data source objects must implement the [`collectionView(_:numberOfItemsInSection:)`](uicollectionviewdatasource/collectionview(_:numberofitemsinsection:).md) and [`collectionView(_:cellForItemAt:)`](uicollectionviewdatasource/collectionview(_:cellforitemat:).md) methods. These methods are responsible for returning the number of items in the collection view along with the items themselves. The remaining methods of the protocol are optional and only needed if your collection view organizes items into multiple sections or provides headers and footers for a given section.

When you configure the collection view object, assign your data source to its [`dataSource`](uicollectionview/datasource.md) property. For more information about how a collection view works with its data source to present content, see [`UICollectionView`](uicollectionview.md).

## Topics

### Getting item and section metrics
- [func collectionView(UICollectionView, numberOfItemsInSection: Int) -> Int](uicollectionviewdatasource/collectionview(_:numberofitemsinsection:).md)
  Asks your data source object for the number of items in the specified section.
- [func numberOfSections(in: UICollectionView) -> Int](uicollectionviewdatasource/numberofsections(in:).md)
  Asks your data source object for the number of sections in the collection view.
### Getting views for items
- [func collectionView(UICollectionView, cellForItemAt: IndexPath) -> UICollectionViewCell](uicollectionviewdatasource/collectionview(_:cellforitemat:).md)
  Asks your data source object for the cell that corresponds to the specified item in the collection view.
- [func collectionView(UICollectionView, viewForSupplementaryElementOfKind: String, at: IndexPath) -> UICollectionReusableView](uicollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:).md)
  Asks your data source object to provide a supplementary view to display in the collection view.
### Reordering items
- [func collectionView(UICollectionView, canMoveItemAt: IndexPath) -> Bool](uicollectionviewdatasource/collectionview(_:canmoveitemat:).md)
  Asks your data source object whether the specified item can move to another location in the collection view.
- [func collectionView(UICollectionView, moveItemAt: IndexPath, to: IndexPath)](uicollectionviewdatasource/collectionview(_:moveitemat:to:).md)
  Tells your data source object to move the specified item to its new location.
### Configuring an index
- [func indexTitles(for: UICollectionView) -> [String]?](uicollectionviewdatasource/indextitles(for:).md)
  Asks the data source to return the titles for the index items to display for the collection view.
- [func collectionView(UICollectionView, indexPathForIndexTitle: String, at: Int) -> IndexPath](uicollectionviewdatasource/collectionview(_:indexpathforindextitle:at:).md)
  Asks the data source to return the index path of a collection view item that corresponds to one of your index entries.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
- [UICollectionViewDiffableDataSourceReference](uicollectionviewdiffabledatasourcereference.md)

## See Also

- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [class UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
  The object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [struct NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md)
  A representation of the state of the data in a layout section at a specific point in time.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource)*