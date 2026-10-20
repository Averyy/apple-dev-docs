# layoutAttributesForCell(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A convenience method for returning the layout attributes for a collection view cell.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func layoutAttributesForCell(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

```objc
- (UICollectionViewLayoutAttributes *) layoutAttributesForCellAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

The collection view layout attributes for the specified collection view cell.

## Parameters

- `indexPath`: The index path for the cell whose layout attributes you want.

## See Also

### Working with collection views
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  A convenience method for returning the layout attributes for a collection view decoration view.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesforsupplementaryview%28ofkind,at%29.md)
  A convenience method for returning the layout attributes for a collection view supplementary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesforcell(at:))*