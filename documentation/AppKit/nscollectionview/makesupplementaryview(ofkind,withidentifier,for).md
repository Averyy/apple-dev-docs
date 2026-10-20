# makeSupplementaryView(ofKind:withIdentifier:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates or returns a reusable supplementary view of the specified type.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func makeSupplementaryView(ofKind elementKind: NSCollectionView.SupplementaryElementKind, withIdentifier identifier: NSUserInterfaceItemIdentifier, for indexPath: IndexPath) -> NSView
```

```objc
- (NSView *) makeSupplementaryViewOfKind:(NSCollectionViewSupplementaryElementKind) elementKind withIdentifier:(NSUserInterfaceItemIdentifier) identifier forIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

A view that adopts the [`NSCollectionViewElement`](../nscollectionviewelement.md) protocol.

#### Discussion

This method looks for a recycled supplementary view of the specified type and returns it if one exists. If one does not exist, it creates it using one of the following techniques:

- If you used the [`register(_:forSupplementaryViewOfKind:withIdentifier:)`](./register%28_,forsupplementaryviewofkind,withidentifier%29-3dqa.md) method to register a class for the identifier, this method instantiates your view class and returns it.
- If you used the [`register(_:forSupplementaryViewOfKind:withIdentifier:)`](./register%28_,forsupplementaryviewofkind,withidentifier%29-7gvf2.md) method to register a nib file for the identifier, this method loads the view from the nib file and returns it.

## Parameters

- `elementKind`: The kind of supplementary view to create. This value is defined by the layout object. This parameter must not be an empty string or `nil`.
- `identifier`: The reuse identifier for the specified item. This is the identifier you specified when registering the supplementary view. This parameter must not be `nil`.
- `indexPath`: The index path specifying the location of the supplementary view. The data source object receives this information in its [`collectionView(_:viewForSupplementaryElementOfKind:at:)`](../nscollectionviewdatasource/collectionview%28_,viewforsupplementaryelementofkind,at%29.md) method and you should just pass it along.

## See Also

### Creating Collection View Items
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, for: IndexPath) -> NSCollectionViewItem](./makeitem%28withidentifier,for%29.md)
  Creates or returns a reusable item object of the specified type.
- [func register(AnyClass?, forItemWithIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemwithidentifier%29-6s4i.md)
  Registers a class to use when creating new items in the collection view.
- [func register(NSNib?, forItemWithIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemwithidentifier%29-90h1i.md)
  Registers a nib file to use when creating items in the collection view.
- [func register(AnyClass?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,forsupplementaryviewofkind,withidentifier%29-3dqa.md)
  Registers a class to use when creating new supplementary views in the collection view.
- [func register(NSNib?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,forsupplementaryviewofkind,withidentifier%29-7gvf2.md)
  Registers a nib file to use when creating supplementary views in the collection view.
- [NSCollectionView.SupplementaryElementKind](./supplementaryelementkind.md)
- [struct NSUserInterfaceItemIdentifier](../nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/makesupplementaryview(ofkind:withidentifier:for:))*