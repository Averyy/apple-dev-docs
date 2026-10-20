# makeItem(withIdentifier:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates or returns a reusable item object of the specified type.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func makeItem(withIdentifier identifier: NSUserInterfaceItemIdentifier, for indexPath: IndexPath) -> NSCollectionViewItem
```

```objc
- (NSCollectionViewItem *) makeItemWithIdentifier:(NSUserInterfaceItemIdentifier) identifier forIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

A valid [`NSCollectionViewItem`](../nscollectionviewitem.md) object.

#### Discussion

This method looks for a recycled item object of the specified type and returns it if one exists. If one does not exist, it creates it using one of the following techniques:

- If you used the [`register(_:forItemWithIdentifier:)`](./register%28_,foritemwithidentifier%29-6s4i.md) method to register a class for the identifier, this method instantiates your class and returns it.
- If you used the [`register(_:forItemWithIdentifier:)`](./register%28_,foritemwithidentifier%29-90h1i.md) method to register a nib file for the identifier, this method loads the item from the nib file and returns it.

## Parameters

- `identifier`: The reuse identifier for the specified item. This is the identifier you specified when registering the item. This parameter must not be `nil`.
- `indexPath`: The index path specifying the location of the item. The data source object receives this information in its [`collectionView(_:itemForRepresentedObjectAt:)`](../nscollectionviewdatasource/collectionview%28_,itemforrepresentedobjectat%29.md) method and you should just pass it along.

## See Also

### Creating Collection View Items
- [func register(AnyClass?, forItemWithIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemwithidentifier%29-6s4i.md)
  Registers a class to use when creating new items in the collection view.
- [func register(NSNib?, forItemWithIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,foritemwithidentifier%29-90h1i.md)
  Registers a nib file to use when creating items in the collection view.
- [func makeSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier, for: IndexPath) -> NSView](./makesupplementaryview%28ofkind,withidentifier,for%29.md)
  Creates or returns a reusable supplementary view of the specified type.
- [func register(AnyClass?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,forsupplementaryviewofkind,withidentifier%29-3dqa.md)
  Registers a class to use when creating new supplementary views in the collection view.
- [func register(NSNib?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](./register%28_,forsupplementaryviewofkind,withidentifier%29-7gvf2.md)
  Registers a nib file to use when creating supplementary views in the collection view.
- [NSCollectionView.SupplementaryElementKind](./supplementaryelementkind.md)
- [struct NSUserInterfaceItemIdentifier](../nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/makeitem(withidentifier:for:))*