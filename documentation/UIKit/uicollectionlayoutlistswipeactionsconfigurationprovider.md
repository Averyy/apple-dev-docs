# UICollectionLayoutListSwipeActionsConfigurationProvider

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures the swipe actions for a cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```c
typedef UISwipeActionsConfiguration *(^)(NSIndexPath *) UICollectionLayoutListSwipeActionsConfigurationProvider;
```

## See Also

### Customizing swipe actions
- [leadingSwipeActionsConfigurationProvider](./uicollectionlayoutlistconfiguration-c.class/leadingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the leading edge of the cell.
- [trailingSwipeActionsConfigurationProvider](./uicollectionlayoutlistconfiguration-c.class/trailingswipeactionsconfigurationprovider.md)
  The closure that provides the set of actions to display when swiping on the trailing edge of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistswipeactionsconfigurationprovider)*