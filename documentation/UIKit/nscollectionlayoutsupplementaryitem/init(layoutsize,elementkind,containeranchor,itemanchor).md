# init(layoutSize:elementKind:containerAnchor:itemAnchor:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a supplementary item of the specified size and element kind, an anchor relative to a container, and an anchor relative to an item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor, itemAnchor: NSCollectionLayoutAnchor)
```

```objc
+ (instancetype) supplementaryItemWithLayoutSize:(NSCollectionLayoutSize *) layoutSize elementKind:(NSString *) elementKind containerAnchor:(NSCollectionLayoutAnchor *) containerAnchor itemAnchor:(NSCollectionLayoutAnchor *) itemAnchor;
```

## See Also

### Creating a supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor)](./init%28layoutsize,elementkind,containeranchor%29.md)
  Creates a supplementary item of the specified size and element kind, with an anchor relative to a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:itemanchor:))*