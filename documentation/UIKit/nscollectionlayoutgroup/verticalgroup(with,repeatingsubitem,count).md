# verticalGroup(with:repeatingSubitem:count:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a group that repeats the specified subitem a certain number of times along the vertical axis.

**Availability**:
- iOS 16.0+ - Deprecated in 16.0 (renamed: vertical(layoutSize:repeatingSubitem:count:))
- iPadOS 16.0+ - Deprecated in 16.0 (renamed: vertical(layoutSize:repeatingSubitem:count:))
- Mac Catalyst 16.0+ - Deprecated in 16.0 (renamed: vertical(layoutSize:repeatingSubitem:count:))
- tvOS
- visionOS

> **Deprecated**: Use [`vertical(layoutSize:repeatingSubitem:count:)`](./vertical%28layoutsize,repeatingsubitem,count%29.md) instead.

## Declaration

```swift
@MainActor
@preconcurrency class func verticalGroup(with size: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup
```

## See Also

### Deprecated
- [class func horizontal(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](./horizontal%28layoutsize,subitem,count%29.md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count.
- [class func horizontalGroup(with: NSCollectionLayoutSize, repeatingSubitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup](./horizontalgroup%28with,repeatingsubitem,count%29.md)
  Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.
- [class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self](./vertical%28layoutsize,subitem,count%29.md)
  Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/verticalgroup(with:repeatingsubitem:count:))*