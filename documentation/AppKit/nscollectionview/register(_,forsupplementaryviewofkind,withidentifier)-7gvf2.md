# register(_:forSupplementaryViewOfKind:withIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers a nib file to use when creating supplementary views in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func register(_ nib: NSNib?, forSupplementaryViewOfKind kind: NSCollectionView.SupplementaryElementKind, withIdentifier identifier: NSUserInterfaceItemIdentifier)
```

```objc
- (void) registerNib:(NSNib *) nib forSupplementaryViewOfKind:(NSCollectionViewSupplementaryElementKind) kind withIdentifier:(NSUserInterfaceItemIdentifier) identifier;
```

#### Discussion

Use this method to register nib files containing prototype supplementary views in your collection view. When you request a view using the [`makeSupplementaryView(ofKind:withIdentifier:for:)`](./makesupplementaryview%28ofkind,withidentifier,for%29.md) method, the collection view recycles an existing view with the same `identifier` and `kind` values or creates a new one by loading the contents of your nib file.

The layout object is responsible for defining the kind of supplementary views it supports and how those views are used. For example, the flow layout ([`NSCollectionViewFlowLayout`](../nscollectionviewflowlayout.md) class) lets you specify supplementary views to act as headers and footers for each section.

Typically, you register your supplementary views when initializing your collection view interface. Although you can register new views at any time, you must not call the [`makeSupplementaryView(ofKind:withIdentifier:for:)`](./makesupplementaryview%28ofkind,withidentifier,for%29.md) method until after you register the corresponding view.

## Parameters

- `nib`: The nib object containing the supplementary view’s definition. The nib file must contain exactly one [`NSView`](../nsview.md) object at the top level and that view must conform to the [`NSCollectionViewElement`](../nscollectionviewelement.md) protocol. Specify `nil` to unregister a previously registered class or nib file.
- `kind`: The kind of the supplementary view. Layout objects define the kinds of supplementary views they support and are responsible for providing appropriate strings that you can pass for this parameter. This parameter must not be an empty string or `nil`.
- `identifier`: The string that identifies the type of supplementary view. You use this string later when requesting new views and it must be unique among the other registered item and view classes of this collection view. This parameter must not be an empty string or `nil`.

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
- [NSCollectionView.SupplementaryElementKind](./supplementaryelementkind.md)
- [struct NSUserInterfaceItemIdentifier](../nsuserinterfaceitemidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/register(_:forsupplementaryviewofkind:withidentifier:)-7gvf2)*