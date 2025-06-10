# verticalGroup(with:repeatingSubitem:count:)

**Framework**: UIKit  
**Kind**: method

Creates a group that repeats the specified subitem a certain number of times along the vertical axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class func verticalGroup(with size: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup
```

## See Also

- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](nscollectionlayoutgroup/horizontal(layoutsize:subitem:count:).md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.
- [class func horizontalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](nscollectionlayoutgroup/horizontalgroup(with:repeatingsubitem:count:).md)
  Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitem:count:).md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/verticalgroup(with:repeatingsubitem:count:))*