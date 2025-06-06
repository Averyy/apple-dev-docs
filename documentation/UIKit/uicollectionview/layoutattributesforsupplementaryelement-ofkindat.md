# layoutAttributesForSupplementaryElement(ofKind:at:)

**Framework**: UIKit  
**Kind**: method

Gets the layout information for the specified supplementary view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func layoutAttributesForSupplementaryElement(ofKind kind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

The layout attributes of the supplementary view or `nil` if the specified supplementary view does not exist.

#### Discussion

Use this method to retrieve the layout information for a particular supplementary view. You should always use this method instead of querying the layout object directly.

## Parameters

- `kind`: A string specifying the kind of supplementary view whose layout attributes you want. Layout classes are responsible for defining the kinds of supplementary views they support.
- `indexPath`: The index path of the supplementary view. The interpretation of this value depends on how the layout implements the view. For example, a view associated with a section might contain just a section value.

## See Also

- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionview/layoutattributesforitem(at:).md)
  Gets the layout information for the item at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/layoutattributesforsupplementaryelement(ofkind:at:))*