# UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that configures the swipe actions for a cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
typealias SwipeActionsConfigurationProvider = (IndexPath) -> UISwipeActionsConfiguration?
```

## See Also

- [var leadingSwipeActionsConfigurationProvider: UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider?](uicollectionlayoutlistconfiguration-swift.struct/leadingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [var trailingSwipeActionsConfigurationProvider: UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider?](uicollectionlayoutlistconfiguration-swift.struct/trailingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the trailing edge of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider)*