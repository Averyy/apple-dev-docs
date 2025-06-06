# vertical(layoutSize:subitem:count:)

**Framework**: AppKit  
**Kind**: method

Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self
```

#### Discussion

When you set a value for the [`interItemSpacing`](nscollectionlayoutgroup/interitemspacing.md) property after using this initializer, the group keeps the same number of items and automatically resizes them to add the extra specified spacing between them.

## See Also

- [class func vertical(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitems:).md)
  Creates a group of the specified size, containing an array of items arranged in a vertical line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup/vertical(layoutsize:subitem:count:))*