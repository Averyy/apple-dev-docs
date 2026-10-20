# UINavigationBarDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Methods that a navigation bar calls before and after it modifies its stack of navigation items.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UINavigationBarDelegate : UIBarPositioningDelegate
```

```objc
@protocol UINavigationBarDelegate <UIBarPositioningDelegate>
```

#### Overview

The [`UINavigationBarDelegate`](./uinavigationbardelegate.md) protocol defines optional methods that a [`UINavigationBar`](./uinavigationbar.md) [`delegate`](./uinavigationbar/delegate.md) implements to update its views when items push or pop from the stack. The navigation bar represents only the bar at the top of the screen, not the view below. It’s the application’s responsibility to implement the behavior when the top item changes.

You can control whether a navigation bar pushes an item on or pops an item from the stack by implementing the [`navigationBar(_:shouldPush:)`](./uinavigationbardelegate/navigationbar%28_,shouldpush%29.md) and [`navigationBar(_:shouldPop:)`](./uinavigationbardelegate/navigationbar%28_,shouldpop%29.md) methods. These methods return [`true`](../Swift/true.md) if the action is allowed; otherwise, [`false`](../Swift/false.md).

The screen always reflects the top item on the navigation bar. You implement the [`navigationBar(_:didPush:)`](./uinavigationbardelegate/navigationbar%28_,didpush%29.md) method to update the view below the navigation bar to reflect the new item. Similarly, you implement the [`navigationBar(_:didPop:)`](./uinavigationbardelegate/navigationbar%28_,didpop%29.md) method to replace the view below the navigation bar.

## Topics

### Pushing items
- [func navigationBar(UINavigationBar, shouldPush: UINavigationItem) -> Bool](./uinavigationbardelegate/navigationbar%28_,shouldpush%29.md)
  Returns a Boolean value indicating whether the navigation bar should push an item.
- [func navigationBar(UINavigationBar, didPush: UINavigationItem)](./uinavigationbardelegate/navigationbar%28_,didpush%29.md)
  Tells the delegate that an item was pushed onto the navigation bar.
### Popping items
- [func navigationBar(UINavigationBar, shouldPop: UINavigationItem) -> Bool](./uinavigationbardelegate/navigationbar%28_,shouldpop%29.md)
  Returns a Boolean value indicating whether the navigation bar should pop an item.
- [func navigationBar(UINavigationBar, didPop: UINavigationItem)](./uinavigationbardelegate/navigationbar%28_,didpop%29.md)
  Tells the delegate that an item was popped from the navigation bar.
### Building with Mac Catalyst
- [func navigationBarNSToolbarSection(UINavigationBar) -> UINavigationBar.NSToolbarSection](./uinavigationbardelegate/navigationbarnstoolbarsection%28_%29.md)
  Asks the delegate which section of the toolbar to host the navigation bar in.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIBarPositioningDelegate](./uibarpositioningdelegate.md)

## See Also

### Responding to navigation bar changes
- [var delegate: (any UINavigationBarDelegate)?](./uinavigationbar/delegate.md)
  The navigation bar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate)*