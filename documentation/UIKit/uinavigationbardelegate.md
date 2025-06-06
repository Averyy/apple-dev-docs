# UINavigationBarDelegate

**Framework**: UIKit  
**Kind**: protocol

Methods that a navigation bar calls before and after it modifies its stack of navigation items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UINavigationBarDelegate : UIBarPositioningDelegate
```

#### Overview

The [`UINavigationBarDelegate`](uinavigationbardelegate.md) protocol defines optional methods that a [`UINavigationBar`](uinavigationbar.md) [`delegate`](uinavigationbar/delegate.md) implements to update its views when items push or pop from the stack. The navigation bar represents only the bar at the top of the screen, not the view below. It’s the application’s responsibility to implement the behavior when the top item changes.

You can control whether a navigation bar pushes an item on or pops an item from the stack by implementing the [`navigationBar(_:shouldPush:)`](uinavigationbardelegate/navigationbar(_:shouldpush:).md) and [`navigationBar(_:shouldPop:)`](uinavigationbardelegate/navigationbar(_:shouldpop:).md) methods. These methods return [`true`](https://developer.apple.com/documentation/swift/true) if the action is allowed; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

The screen always reflects the top item on the navigation bar. You implement the [`navigationBar(_:didPush:)`](uinavigationbardelegate/navigationbar(_:didpush:).md) method to update the view below the navigation bar to reflect the new item. Similarly, you implement the [`navigationBar(_:didPop:)`](uinavigationbardelegate/navigationbar(_:didpop:).md) method to replace the view below the navigation bar.

## Topics

### Pushing items
- [func navigationBar(UINavigationBar, shouldPush: UINavigationItem) -> Bool](uinavigationbardelegate/navigationbar(_:shouldpush:).md)
  Returns a Boolean value indicating whether the navigation bar should push an item.
- [func navigationBar(UINavigationBar, didPush: UINavigationItem)](uinavigationbardelegate/navigationbar(_:didpush:).md)
  Tells the delegate that an item was pushed onto the navigation bar.
### Popping items
- [func navigationBar(UINavigationBar, shouldPop: UINavigationItem) -> Bool](uinavigationbardelegate/navigationbar(_:shouldpop:).md)
  Returns a Boolean value indicating whether the navigation bar should pop an item.
- [func navigationBar(UINavigationBar, didPop: UINavigationItem)](uinavigationbardelegate/navigationbar(_:didpop:).md)
  Tells the delegate that an item was popped from the navigation bar.
### Building with Mac Catalyst
- [func navigationBarNSToolbarSection(UINavigationBar) -> UINavigationBar.NSToolbarSection](uinavigationbardelegate/navigationbarnstoolbarsection(_:).md)
  Asks the delegate which section of the toolbar to host the navigation bar in.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## See Also

- [var delegate: (any UINavigationBarDelegate)?](uinavigationbar/delegate.md)
  The navigation bar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate)*