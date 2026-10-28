# layoutAttributesForSupplementaryView(ofKind:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A convenience method for returning the layout attributes for a collection view supplementary view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func layoutAttributesForSupplementaryView(ofKind kind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

```objc
- (UICollectionViewLayoutAttributes *) layoutAttributesForSupplementaryViewOfKind:(NSString *) kind atIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

The collection view layout attributes for the specified supplementary view.

## Parameters

- `kind`: A string that identifies the type of supplementary view whose layout attributes you want.
- `indexPath`: The index path for the cell whose supplementary view layout attributes you want.

## See Also

### Working with collection views
- [func layoutAttributesForCell(at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesforcell%28at%29.md)
  A convenience method for returning the layout attributes for a collection view cell.
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  A convenience method for returning the layout attributes for a collection view decoration view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesforsupplementaryview(ofkind:at:))*