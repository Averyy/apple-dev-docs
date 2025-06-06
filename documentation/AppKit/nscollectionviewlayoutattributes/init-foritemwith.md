# init(forItemWith:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a layout attributes object for the item at the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
convenience init(forItemWith indexPath: IndexPath)
```

#### Return Value

A new layout attributes object containing the initial attributes for the item.

#### Discussion

Call this method when you need to create a layout attributes object for an item in a collection view. Items are the main type of content presented by a collection view. Items are grouped into sections, although a collection view may have only one section. This method assigns the provided index path to the [`indexPath`](nscollectionviewlayoutattributes/indexpath.md) property of the returned object.

## Parameters

- `indexPath`: The index path of the item. You can use this information to identify the item in your app’s data structures. This parameter must contain a valid value.

## See Also

- [convenience init(forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, with: IndexPath)](nscollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:).md)
  Creates and returns a layout attributes object for a supplementary view based on the specified information.
- [convenience init(forDecorationViewOfKind: NSCollectionView.DecorationElementKind, with: IndexPath)](nscollectionviewlayoutattributes/init(fordecorationviewofkind:with:).md)
  Creates and returns a layout attributes object for a decoration view based on the specified information.
- [convenience init(forInterItemGapBefore: IndexPath)](nscollectionviewlayoutattributes/init(forinteritemgapbefore:).md)
  Creates and returns a layout attributes object for an inter-item gap view at the specified index path.
- [NSCollectionView.DecorationElementKind](nscollectionview/decorationelementkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/init(foritemwith:))*