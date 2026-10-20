# layoutAttributesForDecorationView(ofKind:at:)

**Framework**: UIKit  
**Kind**: method

A convenience method for returning the layout attributes for a collection view decoration view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func layoutAttributesForDecorationView(ofKind decorationViewKind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

The collection view layout attributes for the specified decoration view.

## Parameters

- `decorationViewKind`: The kind identifier for the specified decoration view.
- `indexPath`: The index path for the cell whose decoration view layout attributes you want.

## See Also

- [func layoutAttributesForCell(at: IndexPath) -> UICollectionViewLayoutAttributes?](uidynamicanimator/layoutattributesforcell(at:).md)
  A convenience method for returning the layout attributes for a collection view cell.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uidynamicanimator/layoutattributesforsupplementaryview(ofkind:at:).md)
  A convenience method for returning the layout attributes for a collection view supplementary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesfordecorationview(ofkind:at:))*