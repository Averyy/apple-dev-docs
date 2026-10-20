# horizontal(layoutSize:subitems:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, containing an array of items arranged in a horizontal line.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

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
- [class func horizontal(layoutSize: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> Self](./horizontal%28layoutsize,repeatingsubitem,count%29.md)
  Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/horizontal(layoutsize:subitems:))*