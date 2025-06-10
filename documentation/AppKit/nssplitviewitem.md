# NSSplitViewItem

**Framework**: AppKit  
**Kind**: class

An item in a split view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSSplitViewItem
```

#### Overview

A split view item represents a single pane in a split view controller ([`NSSplitViewController`](nssplitviewcontroller.md)). Each split view item contains information about a child view controller in the split view controller, like its preferred thickness, holding priority, and collapsed state.

To add one or more accessory views to the top or bottom of a split view item, such as a search field above a list, use the [`topAlignedAccessoryViewControllers`](nssplitviewitem/topalignedaccessoryviewcontrollers.md) and [`bottomAlignedAccessoryViewControllers`](nssplitviewitem/bottomalignedaccessoryviewcontrollers.md) properties to specify  [`NSSplitViewItemAccessoryViewController`](nssplitviewitemaccessoryviewcontroller.md) types.

## Topics

### Creating a split view item
- [convenience init(sidebarWithViewController: NSViewController)](nssplitviewitem/init(sidebarwithviewcontroller:).md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(contentListWithViewController: NSViewController)](nssplitviewitem/init(contentlistwithviewcontroller:).md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(viewController: NSViewController)](nssplitviewitem/init(viewcontroller:).md)
  Creates a split view item that represents the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](nssplitviewitem/init(inspectorwithviewcontroller:).md)
### Managing the item thickness
- [var automaticMaximumThickness: CGFloat](nssplitviewitem/automaticmaximumthickness.md)
  The maximum thickness of the split view item when it resizes due to automatic sizing.
- [var preferredThicknessFraction: CGFloat](nssplitviewitem/preferredthicknessfraction.md)
  The preferred thickness of the split view item relative to the split view.
- [var minimumThickness: CGFloat](nssplitviewitem/minimumthickness.md)
  The minimum thickness of the split view item.
- [var maximumThickness: CGFloat](nssplitviewitem/maximumthickness.md)
  The maximum thickness of the split view item.
- [class let unspecifiedDimension: CGFloat](nssplitviewitem/unspecifieddimension.md)
  A constant that resets a dimension’s value.
### Getting Auto Layout behaviors
- [var holdingPriority: NSLayoutConstraint.Priority](nssplitviewitem/holdingpriority.md)
  The priority for a split view item to hold its size.
- [var automaticallyAdjustsSafeAreaInsets: Bool](nssplitviewitem/automaticallyadjustssafeareainsets.md)
  When YES, other items such as sidebars or inspectors may appear overlaid on top of this item’s `viewController` and this item’s `safeAreaInsets` will be adjusted with respect to overlaid content. Defaults to `NO`.
### Getting the item behavior
- [var behavior: NSSplitViewItem.Behavior](nssplitviewitem/behavior-swift.property.md)
  The standard behavior type of the split view item.
- [NSSplitViewItem.Behavior](nssplitviewitem/behavior-swift.enum.md)
  Constants that describe the behavior of the split view item.
### Collapsing and expanding the item
- [var isCollapsed: Bool](nssplitviewitem/iscollapsed.md)
  A Boolean value that determines whether the child view controller that corresponds to the split view item is in a collapsed state in the split view controller.
- [var canCollapse: Bool](nssplitviewitem/cancollapse.md)
  A Boolean value that determines whether a user interaction can collapse the child view controller that corresponds to the split view item.
- [var collapseBehavior: NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.property.md)
  The resizing behavior when the split view item toggles its collapsed state.
- [NSSplitViewItem.CollapseBehavior](nssplitviewitem/collapsebehavior-swift.enum.md)
  Constants that describe the split view item’s collapsing behavior.
- [var isSpringLoaded: Bool](nssplitviewitem/isspringloaded.md)
  A Boolean value that determines whether the split view item can temporarily expand during a drag.
- [var canCollapseFromWindowResize: Bool](nssplitviewitem/cancollapsefromwindowresize.md)
### Customizing appearance
- [var allowsFullHeightLayout: Bool](nssplitviewitem/allowsfullheightlayout.md)
  A Boolean value that indicates whether full-height sidebars appear in the window after you set a style mask.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](nssplitviewitem/titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
### Configuring accessory views
- [var topAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](nssplitviewitem/topalignedaccessoryviewcontrollers.md)
  The following methods allow you to add accessory views to the top/bottom of this splitViewItem. See `NSSplitViewItemAccessoryViewController` for more details.
- [var bottomAlignedAccessoryViewControllers: [NSSplitViewItemAccessoryViewController]](nssplitviewitem/bottomalignedaccessoryviewcontrollers.md)
- [func addTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](nssplitviewitem/addtopalignedaccessoryviewcontroller(_:).md)
- [func insertTopAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](nssplitviewitem/inserttopalignedaccessoryviewcontroller(_:at:).md)
- [func removeTopAlignedAccessoryViewController(at: Int)](nssplitviewitem/removetopalignedaccessoryviewcontroller(at:).md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [func addBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController)](nssplitviewitem/addbottomalignedaccessoryviewcontroller(_:).md)
- [func insertBottomAlignedAccessoryViewController(NSSplitViewItemAccessoryViewController, at: Int)](nssplitviewitem/insertbottomalignedaccessoryviewcontroller(_:at:).md)
- [func removeBottomAlignedAccessoryViewController(at: Int)](nssplitviewitem/removebottomalignedaccessoryviewcontroller(at:).md)
  NOTE: you can use this method, or `-removeFromParentViewController:`, whichever is easier.
- [class NSSplitViewItemAccessoryViewController](nssplitviewitemaccessoryviewcontroller.md)
### Getting the View Controller
- [var viewController: NSViewController](nssplitviewitem/viewcontroller.md)
  The view controller that the split view item represents.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSplitViewController](nssplitviewcontroller.md)
  An object that manages an array of adjacent child views, and has a split view object for managing dividers between those views.
- [class NSSplitView](nssplitview.md)
  A view that arranges two or more views in a linear stack running horizontally or vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem)*