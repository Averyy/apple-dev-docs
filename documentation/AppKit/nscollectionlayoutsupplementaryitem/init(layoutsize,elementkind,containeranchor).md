# init(layoutSize:elementKind:containerAnchor:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a supplementary item of the specified size and element kind, with an anchor relative to a container.

**Availability**:
- macOS 10.15+

## Declaration

```swift
convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor)
```

```objc
+ (instancetype) supplementaryItemWithLayoutSize:(NSCollectionLayoutSize *) layoutSize elementKind:(NSString *) elementKind containerAnchor:(NSCollectionLayoutAnchor *) containerAnchor;
```

## See Also

### Creating a supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor, itemAnchor: NSCollectionLayoutAnchor)](./init%28layoutsize,elementkind,containeranchor,itemanchor%29.md)
  Creates a supplementary item of the specified size and element kind, an anchor relative to a container, and an anchor relative to an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:))*