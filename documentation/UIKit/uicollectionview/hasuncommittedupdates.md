# hasUncommittedUpdates

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasUncommittedUpdates: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), avoid making any significant changes to the collection view. Specifically, don’t reload the collection view’s data, as doing so deletes all placeholders and recreates items from the data source.

## See Also

- [func reconfigureItems(at: [IndexPath])](uicollectionview/reconfigureitems(at:).md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](uicollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](uicollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.
- [func reloadItems(at: [IndexPath])](uicollectionview/reloaditems(at:).md)
  Reloads just the items at the specified index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/hasuncommittedupdates)*