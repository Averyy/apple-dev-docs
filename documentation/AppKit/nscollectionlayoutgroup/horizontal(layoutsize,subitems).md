# horizontal(layoutSize:subitems:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, containing an array of items arranged in a horizontal line.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func horizontal(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self
```

```objc
+ (instancetype) horizontalGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize subitems:(NSArray<NSCollectionLayoutItem *> *) subitems;
```

## Parameters

- `layoutSize`: The group’s size.
- `subitems`: The subitems to include.

## See Also

### Creating a horizontal group
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](./horizontal%28layoutsize,subitem,count%29.md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup/horizontal(layoutsize:subitems:))*