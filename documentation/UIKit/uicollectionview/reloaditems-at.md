# reloadItems(at:)

**Framework**: UIKit  
**Kind**: method

Reloads just the items at the specified index paths.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadItems(at indexPaths: [IndexPath])
```

#### Discussion

Call this method to selectively reload only the specified items. This causes the collection view to discard any cells associated with those items and redisplay them.

## Parameters

- `indexPaths`: An array of   objects identifying the items you want to update.

## See Also

- [var hasUncommittedUpdates: Bool](uicollectionview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](uicollectionview/reconfigureitems(at:).md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](uicollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](uicollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reloaditems(at:))*