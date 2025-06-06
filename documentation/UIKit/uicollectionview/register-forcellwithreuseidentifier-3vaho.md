# register(_:forCellWithReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a class for use in creating new collection view cells.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ cellClass: AnyClass?, forCellWithReuseIdentifier identifier: String)
```

#### Discussion

Prior to calling the [`dequeueReusableCell(withReuseIdentifier:for:)`](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md) method of the collection view, you must use this method or the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md) method to tell the collection view how to create a new cell of the given type. If a cell of the specified type is not currently in a reuse queue, the collection view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the class you specify in the `cellClass` parameter replaces the old entry. You may specify `nil` for `cellClass` if you want to unregister the class from the specified reuse identifier.

## Parameters

- `cellClass`: The class of a cell that you want to use in the collection view.
- `identifier`: The reuse identifier to associate with the specified class. This parameter must not be   and must not be an empty string.

## See Also

- [UICollectionView.CellRegistration](uicollectionview/cellregistration.md)
  A registration for the collection view’s cells.
- [func dequeueConfiguredReusableCell<Cell, Item>(using: UICollectionView.CellRegistration<Cell, Item>, for: IndexPath, item: Item?) -> Cell](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md)
  Dequeues a configured reusable cell object.
- [func register(UINib?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho)*