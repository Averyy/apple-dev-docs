# vertical(layoutSize:repeatingSubitem:count:)

**Framework**: UIKit  
**Kind**: method

Creates a group that repeats the specified subitem a certain number of times along the vertical axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func vertical(layoutSize: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> Self
```

## Parameters

- `layoutSize`: The group’s size.
- `subitem`: The subitem to repeat. It’s your responsibility to ensure that the group’s   can fit   repetitions of this item.
- `count`: The number of times to repeat the subitem.

## See Also

- [class func vertical(layoutSize: NSCollectionLayoutSize, subitems: [NSCollectionLayoutItem]) -> Self](nscollectionlayoutgroup/vertical(layoutsize:subitems:).md)
  Creates a group of the specified size, containing an array of items arranged in a vertical line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/vertical(layoutsize:repeatingsubitem:count:))*