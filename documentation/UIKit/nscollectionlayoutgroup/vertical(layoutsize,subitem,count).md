# vertical(layoutSize:subitem:count:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`vertical(layoutSize:repeatingSubitem:count:)`](./vertical%28layoutsize,repeatingsubitem,count%29.md) instead.

## Declaration

```swift
class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self
```

```objc
+ (instancetype) verticalGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize subitem:(NSCollectionLayoutItem *) subitem count:(NSInteger) count;
```

## Discussion

When you set a value for the [`interItemSpacing`](./interitemspacing.md) property after using this initializer, the group keeps the same number of items and automatically resizes them to add the extra specified spacing between them.

## See Also

### Deprecated
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](./horizontal%28layoutsize,subitem,count%29.md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.
- [class func horizontalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](./horizontalgroup%28with,repeatingsubitem,count%29.md)
  Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.
- [class func verticalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](./verticalgroup%28with,repeatingsubitem,count%29.md)
  Creates a group that repeats the specified subitem a certain number of times along the vertical axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/vertical(layoutsize:subitem:count:))*