# register(_:forCellWithReuseIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers a nib file for use in creating new collection view cells.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func register(_ nib: UINib?, forCellWithReuseIdentifier identifier: String)
```

#### Discussion

Prior to calling the [`dequeueReusableCell(withReuseIdentifier:for:)`](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md) method of the collection view, you must use this method or the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md) method to tell the collection view how to create a new cell of the given type. If a cell of the specified type is not currently in a reuse queue, the collection view uses the provided information to create a new cell object automatically.

If you previously registered a class or nib file with the same reuse identifier, the object you specify in the `nib` parameter replaces the old entry. You may specify `nil` for `nib` if you want to unregister the nib file from the specified reuse identifier.

## Parameters

- `nib`: The nib object containing the cell object. The nib file must contain only one top-level object and that object must be of the type  .
- `identifier`: The reuse identifier to associate with the specified nib file. This parameter must not be   and must not be an empty string.

## See Also

- [UICollectionView.CellRegistration](uicollectionview/cellregistration.md)
  A registration for the collection view’s cells.
- [func dequeueConfiguredReusableCell<Cell, Item>(using: UICollectionView.CellRegistration<Cell, Item>, for: IndexPath, item: Item?) -> Cell](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md)
  Dequeues a configured reusable cell object.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4)*