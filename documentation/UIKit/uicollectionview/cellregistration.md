# UICollectionView.CellRegistration

**Framework**: UIKit  
**Kind**: struct

A registration for the collection view’s cells.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct CellRegistration<Cell, Item> where Cell : UICollectionViewCell
```

#### Overview

Use a cell registration to register cells with your collection view and configure each cell for display. You create a cell registration with your cell type and data item type as the registration’s generic parameters, passing in a registration handler to configure the cell. In the registration handler, you specify how to configure the content and appearance of that type of cell.

The following example creates a cell registration for cells of type [`UICollectionViewListCell`](uicollectionviewlistcell.md). It creates a content configuration with a system default style, customizes the content and appearance of the configuration, and then assigns the configuration to the cell.

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Int> { cell, indexPath, item in
    
    var contentConfiguration = cell.defaultContentConfiguration()
    
    contentConfiguration.text = "\(item)"
    contentConfiguration.textProperties.color = .lightGray
    
    cell.contentConfiguration = contentConfiguration
}
```

After you create a cell registration, you pass it in to [`dequeueConfiguredReusableCell(using:for:item:)`](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md), which you call from your data source’s cell provider.

```swift
dataSource = UICollectionViewDiffableDataSource<Section, Int>(collectionView: collectionView) {
    (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: Int) -> UICollectionViewCell? in
    
    return collectionView.dequeueConfiguredReusableCell(using: cellRegistration,
                                                        for: indexPath,
                                                        item: itemIdentifier)
}
```

You don’t need to call [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md) or [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md). The collection view registers your cell automatically when you pass the cell registration to [`dequeueConfiguredReusableCell(using:for:item:)`](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md).

> ❗ **Important**:  Don’t create your cell registration inside a [`UICollectionViewDiffableDataSource.CellProvider`](uicollectionviewdiffabledatasource-9tqpa/cellprovider.md) closure; doing so prevents cell reuse, and generates an exception in iOS 15 and higher.

 Don’t create your cell registration inside a [`UICollectionViewDiffableDataSource.CellProvider`](uicollectionviewdiffabledatasource-9tqpa/cellprovider.md) closure; doing so prevents cell reuse, and generates an exception in iOS 15 and higher.

## Topics

### Creating a cell registration
- [init(handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](uicollectionview/cellregistration/init(handler:).md)
  Creates a cell registration with the specified registration handler.
- [init(cellNib: UINib, handler: UICollectionView.CellRegistration<Cell, Item>.Handler)](uicollectionview/cellregistration/init(cellnib:handler:).md)
  Creates a cell registration with the specified registration handler and nib file.
- [UICollectionView.CellRegistration.Handler](uicollectionview/cellregistration/handler.md)
  A closure that handles the cell registration and configuration.

## See Also

- [func dequeueConfiguredReusableCell<Cell, Item>(using: UICollectionView.CellRegistration<Cell, Item>, for: IndexPath, item: Item?) -> Cell](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md)
  Dequeues a configured reusable cell object.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cellregistration)*