# UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures the swipe actions for a cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS

## Declaration

```swift
typealias SwipeActionsConfigurationProvider = (IndexPath) -> UISwipeActionsConfiguration?
```

## See Also

### Customizing swipe actions
- [var leadingSwipeActionsConfigurationProvider: UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider?](./leadingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [var trailingSwipeActionsConfigurationProvider: UICollectionLayoutListConfiguration.SwipeActionsConfigurationProvider?](./trailingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the trailing edge of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/swipeactionsconfigurationprovider)*