# dequeueConfiguredReusableCell(using:for:item:)

**Framework**: UIKit  
**Kind**: method

Dequeues a configured reusable cell object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func dequeueConfiguredReusableCell<Cell, Item>(using registration: UICollectionView.CellRegistration<Cell, Item>, for indexPath: IndexPath, item: Item?) -> Cell where Cell : UICollectionViewCell
```

#### Return Value

A configured reusable cell object.

## Parameters

- `registration`: The cell registration for configuring the cell object. See  .
- `indexPath`: The index path that specifies the location of the cell in the collection view.
- `item`: The item that provides data for the cell.

## See Also

- [UICollectionView.CellRegistration](uicollectionview/cellregistration.md)
  A registration for the collection view’s cells.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablecell(using:for:item:))*