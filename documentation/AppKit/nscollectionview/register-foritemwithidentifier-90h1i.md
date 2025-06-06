# register(_:forItemWithIdentifier:)

**Framework**: AppKit  
**Kind**: method

Registers a nib file to use when creating items in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func register(_ nib: NSNib?, forItemWithIdentifier identifier: NSUserInterfaceItemIdentifier)
```

#### Discussion

Use this method to register nib files containing prototype items to use in your collection view. When you request an item using the [`makeItem(withIdentifier:for:)`](nscollectionview/makeitem(withidentifier:for:).md) method, the collection view recycles an existing item with the same `identifier` or creates a new one by loading the contents of your nib file.

Because items are recycled to improve performance, it is recommended that your custom item classes conform to the [`NSCollectionViewElement`](nscollectionviewelement.md) protocol. You can use the methods of that protocol to prepare your classes for reuse.

Typically, you register your items when initializing your collection view interface. Although you can register new items at any time, you must not call the [`makeItem(withIdentifier:for:)`](nscollectionview/makeitem(withidentifier:for:).md) method until after you register the corresponding item.

## Parameters

- `nib`: The nib object containing the item’s definition. The nib file must contain exactly one   object at the top level. You may use a custom subclass when configuring the object in the nib file. Specify   to unregister a previously registered class or nib file.
- `identifier`: The string that identifies the type of item. You use this string later when requesting new items and it must be unique among the other registered item and view classes of this collection view. This parameter must not be an empty string or  .

## See Also

- [func makeItem(withIdentifier: NSUserInterfaceItemIdentifier, for: IndexPath) -> NSCollectionViewItem](nscollectionview/makeitem(withidentifier:for:).md)
  Creates or returns a reusable item object of the specified type.
- [func register(AnyClass?, forItemWithIdentifier: NSUserInterfaceItemIdentifier)](nscollectionview/register(_:foritemwithidentifier:)-6s4i.md)
  Registers a class to use when creating new items in the collection view.
- [func makeSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier, for: IndexPath) -> NSView](nscollectionview/makesupplementaryview(ofkind:withidentifier:for:).md)
  Creates or returns a reusable supplementary view of the specified type.
- [func register(AnyClass?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](nscollectionview/register(_:forsupplementaryviewofkind:withidentifier:)-3dqa.md)
  Registers a class to use when creating new supplementary views in the collection view.
- [func register(NSNib?, forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, withIdentifier: NSUserInterfaceItemIdentifier)](nscollectionview/register(_:forsupplementaryviewofkind:withidentifier:)-7gvf2.md)
  Registers a nib file to use when creating supplementary views in the collection view.
- [NSCollectionView.SupplementaryElementKind](nscollectionview/supplementaryelementkind.md)
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/register(_:foritemwithidentifier:)-90h1i)*