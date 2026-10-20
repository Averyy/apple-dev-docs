# vertical(layoutSize:subitems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, containing an array of items arranged in a vertical line.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func vertical(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self
```

```objc
+ (instancetype) verticalGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize subitems:(NSArray<NSCollectionLayoutItem *> *) subitems;
```

## Parameters

- `layoutSize`: The group’s size.
- `subitems`: The subitems to include.

## See Also

### Creating a vertical group
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](./vertical%28layoutsize,subitem,count%29.md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup/vertical(layoutsize:subitems:))*