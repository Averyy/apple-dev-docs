# UICollectionViewCellRegistration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A registration for the collection view’s cells.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICollectionViewCellRegistration : NSObject
```

## Overview

Use a cell registration to register cells with your collection view and configure each cell for display. You create a cell registration with your cell type and data item type as the registration’s generic parameters, passing in a registration handler to configure the cell. In the registration handler, you specify how to configure the content and appearance of that type of cell.

The following example creates a cell registration for cells of type [`UICollectionViewListCell`](./uicollectionviewlistcell.md). It creates a content configuration with a system default style, customizes the content and appearance of the configuration, and then assigns the configuration to the cell.

```objc
UICollectionViewCellRegistration *cellRegistration = [UICollectionViewCellRegistration registrationWithCellClass:[UICollectionViewListCell class] configurationHandler:^(UICollectionViewListCell *cell, NSIndexPath *indexPath, id item) {
    UIListContentConfiguration *contentConfiguration = cell.defaultContentConfiguration;
    
    contentConfiguration.text = [NSString stringWithFormat:@"%@", item];
    contentConfiguration.textProperties.color = UIColor.lightGrayColor;
    
    cell.contentConfiguration = contentConfiguration;
}];
```

After you create a cell registration, you pass it in to [`dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:`](./uicollectionview/dequeueconfiguredreusablecellwithregistration_forindexpath_item_.md), which you call from your data source’s cell provider.

```objc
self.dataSource = [[UICollectionViewDiffableDataSource alloc] initWithCollectionView:self.collectionView cellProvider:^UICollectionViewCell *(UICollectionView *collectionView, NSIndexPath *indexPath, id item) {
    return [collectionView dequeueConfiguredReusableCellWithRegistration:cellRegistration forIndexPath:indexPath item:item];
}];
```

You don’t need to call [`register(_:forCellWithReuseIdentifier:)`](./uicollectionview/register%28_,forcellwithreuseidentifier%29-6z6t4.md) or [`register(_:forCellWithReuseIdentifier:)`](./uicollectionview/register%28_,forcellwithreuseidentifier%29-3vaho.md). The collection view registers your cell automatically when you pass the cell registration to [`dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:`](./uicollectionview/dequeueconfiguredreusablecellwithregistration_forindexpath_item_.md).

> ❗ **Important**:  Don’t create your cell registration inside a [`UICollectionViewDiffableDataSourceReferenceCellProvider`](./uicollectionviewdiffabledatasourcereferencecellprovider.md) closure; doing so prevents cell reuse, and generates an exception in iOS 15 and higher.

## Topics

### Creating a cell registration
- [+ registrationWithCellClass:configurationHandler:](./uicollectionviewcellregistration/registrationwithcellclass_configurationhandler_.md)
  Creates a cell registration with the specified registration handler.
- [+ registrationWithCellNib:configurationHandler:](./uicollectionviewcellregistration/registrationwithcellnib_configurationhandler_.md)
  Creates a cell registration with the specified registration handler and nib file.
- [UICollectionViewCellRegistrationConfigurationHandler](./uicollectionviewcellregistrationconfigurationhandler.md)
  A closure that handles the cell registration and configuration.
### Querying a cell registration
- [configurationHandler](./uicollectionviewcellregistration/configurationhandler.md)
  The closure that handles the cell registration and configuration.
- [cellClass](./uicollectionviewcellregistration/cellclass.md)
  The class associated with the cell.
- [cellNib](./uicollectionviewcellregistration/cellnib.md)
  The nib file associated with the cell.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Creating cells
- [- dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:](./uicollectionview/dequeueconfiguredreusablecellwithregistration_forindexpath_item_.md)
  Dequeues a configured reusable cell object.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](./uicollectionview/register%28_,forcellwithreuseidentifier%29-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](./uicollectionview/register%28_,forcellwithreuseidentifier%29-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](./uicollectionview/dequeuereusablecell%28withreuseidentifier,for%29.md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcellregistration)*