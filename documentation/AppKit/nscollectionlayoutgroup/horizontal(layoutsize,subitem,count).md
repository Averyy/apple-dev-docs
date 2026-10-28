# horizontal(layoutSize:subitem:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self
```

```objc
+ (instancetype) horizontalGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize subitem:(NSCollectionLayoutItem *) subitem count:(NSInteger) count;
```

## Discussion

When you set a value for the [`interItemSpacing`](./interitemspacing.md) property after using this initializer, the group keeps the same number of items and automatically resizes them to add the extra specified spacing between them.

## See Also

### Creating a horizontal group
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](./horizontal%28layoutsize,subitems%29.md)
  Creates a group of the specified size, containing an array of items arranged in a horizontal line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup/horizontal(layoutsize:subitem:count:))*