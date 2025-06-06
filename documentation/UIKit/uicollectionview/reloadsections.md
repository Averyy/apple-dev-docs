# reloadSections(_:)

**Framework**: UIKit  
**Kind**: method

Reloads the data in the specified sections of the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadSections(_ sections: IndexSet)
```

#### Discussion

Call this method to selectively reload only the items in the specified sections. This causes the collection view to discard any cells associated with those items and redisplay them. This method also discards any placeholders in the specified sections.

## Parameters

- `sections`: The indexes of the sections to reload.

## See Also

- [var hasUncommittedUpdates: Bool](uicollectionview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](uicollectionview/reconfigureitems(at:).md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](uicollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadItems(at: [IndexPath])](uicollectionview/reloaditems(at:).md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reloadsections(_:))*