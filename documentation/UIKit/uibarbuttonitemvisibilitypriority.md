# UIBarButtonItemVisibilityPriority

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct UIBarButtonItemVisibilityPriority
```

```c
typedef NSInteger UIBarButtonItemVisibilityPriority;
```

## Topics

### Creating a visibility priority
- [init(Int)](./uibarbuttonitemvisibilitypriority/init%28_%29.md)
- [init(higherThan: UIBarButtonItemVisibilityPriority)](./uibarbuttonitemvisibilitypriority/init%28higherthan%29.md)
- [init(lowerThan: UIBarButtonItemVisibilityPriority)](./uibarbuttonitemvisibilitypriority/init%28lowerthan%29.md)
- [init(rawValue: Int)](./uibarbuttonitemvisibilitypriority/init%28rawvalue%29.md)
### Getting visibility priorities
- [static let high: UIBarButtonItemVisibilityPriority](./uibarbuttonitemvisibilitypriority/high.md)
- [static let low: UIBarButtonItemVisibilityPriority](./uibarbuttonitemvisibilitypriority/low.md)
- [static let standard: UIBarButtonItemVisibilityPriority](./uibarbuttonitemvisibilitypriority/standard.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bars
- [class UIBarItem](./uibaritem.md)
  An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.
- [class UIBarButtonItem](./uibarbuttonitem.md)
  A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.
- [class UIBarButtonItemGroup](./uibarbuttonitemgroup.md)
  A group of one or more bar button items for placement on a navigation bar or shortcuts bar.
- [class UINavigationBar](./uinavigationbar.md)
  A region that displays the title and controls provided by navigation items.
- [class UISearchBar](./uisearchbar.md)
  A specialized view for receiving search-related information from the user.
- [class UIToolbar](./uitoolbar.md)
  A control that displays one or more buttons along an edge of your interface.
- [class UITabBar](./uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](./uitabbaritem.md)
  An object that describes an item in a tab bar.
- [protocol UIBarPositioning](./uibarpositioning.md)
  A set of methods for defining the positioning of bars in iOS apps.
- [protocol UIBarPositioningDelegate](./uibarpositioningdelegate.md)
  A set of methods that support the positioning of a bar that conforms to the [`UIBarPositioning`](./uibarpositioning.md) protocol.
- [struct UIBarMinimization](./uibarminimization-swift.struct.md)
- [enum UIVerticalBarEdge](./uiverticalbaredge.md)
  The edge where the system places the vertical bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority)*