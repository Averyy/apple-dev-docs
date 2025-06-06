# layoutAttributesForItem(at:)

**Framework**: AppKit  
**Kind**: method

Returns the layout information for the item at the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func layoutAttributesForItem(at indexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

#### Return Value

The layout attributes of the item or `nil` if no item exists at the specified path.

#### Discussion

This method updates the layout information as needed before returning the specified attributes. Always use this method to retrieve the layout attributes for items in the collection view. Do not query the layout object directly.

## Parameters

- `indexPath`: The index path of the item.

## See Also

- [func layoutAttributesForSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionview/layoutattributesforsupplementaryelement(ofkind:at:).md)
  Returns the layout information for the supplementary view at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/layoutattributesforitem(at:))*