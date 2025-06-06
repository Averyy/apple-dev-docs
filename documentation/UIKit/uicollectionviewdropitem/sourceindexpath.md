# sourceIndexPath

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The index path of the item in the collection view, if any.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceIndexPath: IndexPath? { get }
```

#### Discussion

If the item originated from the collection view, this property contains the item’s original index path.

## See Also

- [var previewSize: CGSize](uicollectionviewdropitem/previewsize.md)
  The size of the drag item’s preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropitem/sourceindexpath)*