# horizontal(layoutSize:repeatingSubitem:count:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class func horizontal(layoutSize: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> Self
```

```objc
+ (instancetype) horizontalGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize repeatingSubitem:(NSCollectionLayoutItem *) subitem count:(NSInteger) count;
```

## Parameters

- `layoutSize`: The group’s size.
- `subitem`: The subitem to repeat. It’s your responsibility to ensure that the group’s `layoutSize` can fit `count` repetitions of this item.
- `count`: The number of times to repeat the subitem.

## See Also

### Creating a horizontal group
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](./horizontal%28layoutsize,subitems%29.md)
  Creates a group of the specified size, containing an array of items arranged in a horizontal line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/horizontal(layoutsize:repeatingsubitem:count:))*