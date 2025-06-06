# layoutAttributesForSupplementaryElement(ofKind:at:)

**Framework**: AppKit  
**Kind**: method

Returns the layout information for the supplementary view at the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func layoutAttributesForSupplementaryElement(ofKind kind: NSCollectionView.SupplementaryElementKind, at indexPath: IndexPath) -> NSCollectionViewLayoutAttributes?
```

#### Return Value

The layout attributes of the supplementary view or `nil` if no item exists at the specified path.

#### Discussion

This method updates the layout information as needed before returning the specified attributes. Always use this method to retrieve the layout attributes for supplementary views in the collection view. Do not query the layout object directly.

## Parameters

- `kind`: The kind of the supplementary view whose attributes you want. The layout object defines the kinds of supplementary views it supports. This parameter must not be  .
- `indexPath`: The index path of the supplementary view. Normally, this path

## See Also

- [func layoutAttributesForItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionview/layoutattributesforitem(at:).md)
  Returns the layout information for the item at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/layoutattributesforsupplementaryelement(ofkind:at:))*