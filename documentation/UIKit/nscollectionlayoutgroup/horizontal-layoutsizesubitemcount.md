# horizontal(layoutSize:subitem:count:)

**Framework**: UIKit  
**Kind**: method

Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self
```

#### Discussion

When you set a value for the [`interItemSpacing`](nscollectionlayoutgroup/interitemspacing.md) property after using this initializer, the group keeps the same number of items and automatically resizes them to add the extra specified spacing between them.

## See Also

- [class func horizontalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](nscollectionlayoutgroup/horizontalgroup(with:repeatingsubitem:count:).md)
  Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitem:count:).md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.
- [class func verticalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](nscollectionlayoutgroup/verticalgroup(with:repeatingsubitem:count:).md)
  Creates a group that repeats the specified subitem a certain number of times along the vertical axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/horizontal(layoutsize:subitem:count:))*