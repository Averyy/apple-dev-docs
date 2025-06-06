# UICollectionView.SupplementaryRegistration

**Framework**: UIKit  
**Kind**: struct

A registration for the collection view’s supplementary views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct SupplementaryRegistration<Supplementary> where Supplementary : UICollectionReusableView
```

#### Overview

Use a supplementary registration to register supplementary views, like headers and footers, with your collection view and configure each view for display. You create a supplementary registration with your supplementary view type and data item type as the registration’s generic parameters, passing in a registration handler to configure the view. In the registration handler, you specify how to configure the content and appearance of that type of supplementary view.

The following example creates a supplementary registration for a custom header view subclass.

```swift
let headerRegistration = UICollectionView.SupplementaryRegistration
    <HeaderView>(elementKind: "Header") {
    supplementaryView, string, indexPath in
    supplementaryView.label.text = "\(string) for section \(indexPath.section)"
    supplementaryView.backgroundColor = .lightGray
}
```

After you create a supplementary registration, you pass it in to [`dequeueConfiguredReusableSupplementary(using:for:)`](uicollectionview/dequeueconfiguredreusablesupplementary(using:for:).md), which you call from your data source’s [`supplementaryViewProvider`](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md).

```swift
dataSource.supplementaryViewProvider = { collectionView, elementKind, indexPath in
    return collectionView.dequeueConfiguredReusableSupplementary(using: headerRegistration,
                                                                 for: indexPath)
}
```

You don’t need to call [`register(_:forSupplementaryViewOfKind:withReuseIdentifier:)`](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io.md) or [`register(_:forSupplementaryViewOfKind:withReuseIdentifier:)`](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md). The registration occurs automatically when you pass the supplementary view registration to [`dequeueConfiguredReusableSupplementary(using:for:)`](uicollectionview/dequeueconfiguredreusablesupplementary(using:for:).md).

> ❗ **Important**:  Don’t create your supplementary view registration inside a [`UICollectionViewDiffableDataSource.SupplementaryViewProvider`](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.md) closure; doing so prevents reuse, and generates an exception in iOS 15 and higher.

 Don’t create your supplementary view registration inside a [`UICollectionViewDiffableDataSource.SupplementaryViewProvider`](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.md) closure; doing so prevents reuse, and generates an exception in iOS 15 and higher.

## Topics

### Creating a supplementary registration
- [init(elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](uicollectionview/supplementaryregistration/init(elementkind:handler:).md)
  Creates a supplementary registration for the specified element kind with a registration handler.
- [init(supplementaryNib: UINib, elementKind: String, handler: UICollectionView.SupplementaryRegistration<Supplementary>.Handler)](uicollectionview/supplementaryregistration/init(supplementarynib:elementkind:handler:).md)
  Creates a supplementary registration for the specified element kind with a registration handler and nib file.
- [UICollectionView.SupplementaryRegistration.Handler](uicollectionview/supplementaryregistration/handler.md)
  A closure that handles the supplementary view registration and configuration.

## See Also

- [func dequeueConfiguredReusableSupplementary<Supplementary>(using: UICollectionView.SupplementaryRegistration<Supplementary>, for: IndexPath) -> Supplementary](uicollectionview/dequeueconfiguredreusablesupplementary(using:for:).md)
  Dequeues a configured reusable supplementary view object.
- [func register(AnyClass?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io.md)
  Registers a class for use in creating supplementary views for the collection view.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [func dequeueReusableSupplementaryView(ofKind: String, withReuseIdentifier: String, for: IndexPath) -> UICollectionReusableView](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md)
  Dequeues a reusable supplementary view located by its identifier and kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/supplementaryregistration)*