# init(forSupplementaryViewOfKind:with:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a layout attributes object for a supplementary view based on the specified information.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(forSupplementaryViewOfKind elementKind: NSCollectionView.SupplementaryElementKind, with indexPath: IndexPath)
```

```objc
+ (instancetype) layoutAttributesForSupplementaryViewOfKind:(NSCollectionViewSupplementaryElementKind) elementKind withIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

A new layout attributes object configured with the initial attributes for the supplementary view.

## Discussion

Call this method when you need to create a layout attributes object for a supplementary view in a collection view. Supplementary views are a secondary type of content that display data related to a specific section. For example, header and footer views in a grid layout implemented using supplementary views. This method uses the parameters to set the initial values of the [`indexPath`](./indexpath.md) and [`representedElementKind`](./representedelementkind.md) properties the returned object.

## Parameters

- `elementKind`: A string that identifies the type of the supplementary view. Use this string to differentiate from among the supplementary views in a given section. This parameter must contain a valid value.
- `indexPath`: The index path of the item. You can use this information to identify the item in your app’s data structures. This parameter must contain a valid value.

## See Also

### Creating Layout Attributes
- [convenience init(forItemWith: IndexPath)](./init%28foritemwith%29.md)
  Creates and returns a layout attributes object for the item at the specified index path.
- [convenience init(forDecorationViewOfKind: NSCollectionView.DecorationElementKind, with: IndexPath)](./init%28fordecorationviewofkind,with%29.md)
  Creates and returns a layout attributes object for a decoration view based on the specified information.
- [convenience init(forInterItemGapBefore: IndexPath)](./init%28forinteritemgapbefore%29.md)
  Creates and returns a layout attributes object for an inter-item gap view at the specified index path.
- [NSCollectionView.DecorationElementKind](../nscollectionview/decorationelementkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:))*