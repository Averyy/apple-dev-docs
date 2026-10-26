# dequeueConfiguredReusableCellWithRegistration:forIndexPath:item:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dequeues a configured reusable cell object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (UICollectionViewCell *) dequeueConfiguredReusableCellWithRegistration:(UICollectionViewCellRegistration *) registration forIndexPath:(NSIndexPath *) indexPath item:(id) item;
```

#### Return Value

A configured reusable cell object.

## Parameters

- `registration`: The cell registration for configuring the cell object. See [`UICollectionViewCellRegistration`](../uicollectionviewcellregistration.md).
- `indexPath`: The index path that specifies the location of the cell in the collection view.
- `item`: The item that provides data for the cell.

## See Also

### Creating cells
- [UICollectionViewCellRegistration](../uicollectionviewcellregistration.md)
  A registration for the collection view’s cells.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](./register%28_,forcellwithreuseidentifier%29-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](./register%28_,forcellwithreuseidentifier%29-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](./dequeuereusablecell%28withreuseidentifier,for%29.md)
  Dequeues a reusable cell object located by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dequeueconfiguredreusablecellwithregistration:forindexpath:item:)*