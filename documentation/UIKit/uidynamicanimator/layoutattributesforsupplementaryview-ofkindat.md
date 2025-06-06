# layoutAttributesForSupplementaryView(ofKind:at:)

**Framework**: UIKit  
**Kind**: method

A convenience method for returning the layout attributes for a collection view supplementary view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func layoutAttributesForSupplementaryView(ofKind kind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

The collection view layout attributes for the specified supplementary view.

## Parameters

- `kind`: A string that identifies the type of supplementary view whose layout attributes you want.
- `indexPath`: The index path for the cell whose supplementary view layout attributes you want.

## See Also

- [func layoutAttributesForCell(at: IndexPath) -> UICollectionViewLayoutAttributes?](uidynamicanimator/layoutattributesforcell(at:).md)
  A convenience method for returning the layout attributes for a collection view cell.
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uidynamicanimator/layoutattributesfordecorationview(ofkind:at:).md)
  A convenience method for returning the layout attributes for a collection view decoration view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesforsupplementaryview(ofkind:at:))*