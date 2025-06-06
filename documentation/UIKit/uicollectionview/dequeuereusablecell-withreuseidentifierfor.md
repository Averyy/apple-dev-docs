# dequeueReusableCell(withReuseIdentifier:for:)

**Framework**: UIKit  
**Kind**: method

Dequeues a reusable cell object located by its identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dequeueReusableCell(withReuseIdentifier identifier: String, for indexPath: IndexPath) -> UICollectionViewCell
```

#### Return Value

A valid [`UICollectionReusableView`](uicollectionreusableview.md) object.

#### Discussion

Call this method from your data source object when asked to provide a new cell for the collection view. This method dequeues an existing cell if one is available or creates a new one based on the class or nib file you previously registered.

> ❗ **Important**:  You must register a class or nib file using the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md) or [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md) method before calling this method.

 You must register a class or nib file using the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md) or [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md) method before calling this method.

If you registered a class for the specified `identifier` and a new cell must be created, this method initializes the cell by calling its [`init(frame:)`](uiview/init(frame:).md) method. For nib-based cells, this method loads the cell object from the provided nib file. If an existing cell was available for reuse, this method calls the cell’s [`prepareForReuse()`](uicollectionreusableview/prepareforreuse().md) method instead.

## Parameters

- `identifier`: The reuse identifier for the specified cell. This parameter must not be  .
- `indexPath`: The index path specifying the location of the cell. The data source receives this information when it is asked for the cell and should just pass it along. This method uses the index path to perform additional configuration based on the cell’s position in the collection view.

## See Also

- [UICollectionView.CellRegistration](uicollectionview/cellregistration.md)
  A registration for the collection view’s cells.
- [func dequeueConfiguredReusableCell<Cell, Item>(using: UICollectionView.CellRegistration<Cell, Item>, for: IndexPath, item: Item?) -> Cell](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md)
  Dequeues a configured reusable cell object.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeuereusablecell(withreuseidentifier:for:))*