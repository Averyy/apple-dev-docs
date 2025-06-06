# layoutAttributesForItem(at:)

**Framework**: UIKit  
**Kind**: method

Gets the layout information for the item at the specified index path.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func layoutAttributesForItem(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

The layout attributes for the item or `nil` if no item exists at the specified path.

#### Discussion

Use this method to retrieve the layout information for a particular item. You should always use this method instead of querying the layout object directly.

## Parameters

- `indexPath`: The index path of the item.

## See Also

- [func layoutAttributesForSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionview/layoutattributesforsupplementaryelement(ofkind:at:).md)
  Gets the layout information for the specified supplementary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/layoutattributesforitem(at:))*