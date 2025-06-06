# reloadData()

**Framework**: UIKit  
**Kind**: method

Reloads all of the data for the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadData()
```

#### Discussion

Call this method sparingly when you need to reload all of the items in the collection view. This causes the collection view to discard any currently visible items (including placeholders) and recreate items based on the current state of the data source object. For efficiency, the collection view only displays those cells and supplementary views that are visible. If the collection data shrinks as a result of the reload, the collection view adjusts its scrolling offsets accordingly.

You shouldn’t call this method in the middle of animation blocks where items are being inserted or deleted. Insertions and deletions automatically cause the collection’s data to be updated appropriately.

## See Also

- [var hasUncommittedUpdates: Bool](uicollectionview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](uicollectionview/reconfigureitems(at:).md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadSections(IndexSet)](uicollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.
- [func reloadItems(at: [IndexPath])](uicollectionview/reloaditems(at:).md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reloaddata())*