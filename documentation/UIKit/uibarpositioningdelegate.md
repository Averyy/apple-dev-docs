# UIBarPositioningDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods that support the positioning of a bar that conforms to the [`UIBarPositioning`](uibarpositioning.md) protocol.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIBarPositioningDelegate : NSObjectProtocol
```

#### Overview

Navigation bars, toolbars, and search bars all have delegates that support the [`UIBarPositioning`](uibarpositioning.md) protocol. The delegate can use the method of this protocol to specify the bar’s position when that bar is moved to a window. The [`UINavigationBarDelegate`](uinavigationbardelegate.md), [`UISearchBarDelegate`](uisearchbardelegate.md), and [`UIToolbarDelegate`](uitoolbardelegate.md) protocols extend this protocol to allow for the positioning of those bars on the screen.

## Topics

### Positioning Bars
- [func position(for: any UIBarPositioning) -> UIBarPosition](uibarpositioningdelegate/position(for:).md)
  Asks the delegate for the position of the specified bar in its new window.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UINavigationBarDelegate](uinavigationbardelegate.md)
- [UISearchBarDelegate](uisearchbardelegate.md)
- [UIToolbarDelegate](uitoolbardelegate.md)

## See Also

- [class UIBarItem](uibaritem.md)
  An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.
- [class UIBarButtonItem](uibarbuttonitem.md)
  A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.
- [class UIBarButtonItemGroup](uibarbuttonitemgroup.md)
  A group of one or more bar button items for placement on a navigation bar or shortcuts bar.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UISearchBar](uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [class UIToolbar](uitoolbar.md)
  A control that displays one or more buttons along an edge of your interface.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [protocol UIBarPositioning](uibarpositioning.md)
  A set of methods for defining the positioning of bars in iOS apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarpositioningdelegate)*