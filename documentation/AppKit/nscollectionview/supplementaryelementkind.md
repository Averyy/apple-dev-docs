# NSCollectionView.SupplementaryElementKind

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias SupplementaryElementKind = String
```

```c
typedef NSString * NSCollectionViewSupplementaryElementKind;
```

## See Also

### Creating Collection View Items
- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, for: IndexPath) -> NSCollectionViewItem](./makeitem%28withidentifier,for%29.md)
  Creates or returns a reusable item object of the specified type.
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
- [struct NSUserInterfaceItemIdentifier](../nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/supplementaryelementkind)*