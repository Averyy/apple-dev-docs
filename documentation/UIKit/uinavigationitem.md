# UINavigationItem

**Framework**: UIKit  
**Kind**: class

The items that a navigation bar displays when the associated view controller is visible.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UINavigationItem
```

#### Overview

When building a navigation interface, each view controller that you push onto the navigation stack must have a [`UINavigationItem`](uinavigationitem.md) object that contains the buttons and views you want to display in the navigation bar. The managing [`UINavigationController`](uinavigationcontroller.md) object uses the navigation items of the topmost two view controllers to populate the navigation bar with content.

A navigation item always reflects information about its associated view controller. The navigation item must provide a title to display when the view controller is topmost on the navigation stack. The item can also contain additional buttons to display on the right (or trailing) side of the navigation bar. You can specify buttons and views to display on the left (or leading) side of the toolbar using the [`leftBarButtonItems`](uinavigationitem/leftbarbuttonitems.md) property, but the navigation controller displays those buttons only when space is available.

The [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md) property of a navigation item reflects the Back button you want to display when the current view controller is just below the topmost view controller. The Back button doesn’t appear when the current view controller is topmost.

When specifying buttons for a navigation item, you must use [`UIBarButtonItem`](uibarbuttonitem.md) objects. If you want to display custom views in the navigation bar, you must wrap those views inside a [`UIBarButtonItem`](uibarbuttonitem.md) object before adding them to the navigation item.

## Topics

### Initializing an item
- [init(title: String)](uinavigationitem/init(title:).md)
  Creates a navigation item with the specified title.
- [init?(coder: NSCoder)](uinavigationitem/init(coder:).md)
  Creates a navigation item from data in an unarchiver.
### Configuring the title
- [var title: String?](uinavigationitem/title.md)
  The navigation item’s title that displays in the navigation bar.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.
### Configuring the Back button
- [var backBarButtonItem: UIBarButtonItem?](uinavigationitem/backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](uinavigationitem/backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [var hidesBackButton: Bool](uinavigationitem/hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](uinavigationitem/sethidesbackbutton(_:animated:).md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](uinavigationitem/backaction.md)
  The back action for the navigation bar.
### Specifying the navigation style
- [var style: UINavigationItem.ItemStyle](uinavigationitem/style.md)
  A style that determines how the content of the navigation item lays out in the navigation bar.
- [UINavigationItem.ItemStyle](uinavigationitem/itemstyle.md)
  Constants that determine how the content of the navigation item lays out in the navigation bar.
### Specifying custom views
- [var centerItemGroups: [UIBarButtonItemGroup]](uinavigationitem/centeritemgroups.md)
  Customizable item groups to display in the center section of the navigation bar.
- [var leadingItemGroups: [UIBarButtonItemGroup]](uinavigationitem/leadingitemgroups.md)
  Item groups to display in the leading section of the navigation bar.
- [var trailingItemGroups: [UIBarButtonItemGroup]](uinavigationitem/trailingitemgroups.md)
  Item groups to display in the trailing section of the navigation bar.
- [var pinnedTrailingGroup: UIBarButtonItemGroup?](uinavigationitem/pinnedtrailinggroup.md)
  The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [var titleView: UIView?](uinavigationitem/titleview.md)
  A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [var leftBarButtonItems: [UIBarButtonItem]?](uinavigationitem/leftbarbuttonitems.md)
  An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [var leftBarButtonItem: UIBarButtonItem?](uinavigationitem/leftbarbuttonitem.md)
  A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItems: [UIBarButtonItem]?](uinavigationitem/rightbarbuttonitems.md)
  An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [var rightBarButtonItem: UIBarButtonItem?](uinavigationitem/rightbarbuttonitem.md)
  A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [func setLeftBarButtonItems([UIBarButtonItem]?, animated: Bool)](uinavigationitem/setleftbarbuttonitems(_:animated:).md)
  Sets the left bar button items, optionally animating the transition to the new items.
- [func setLeftBarButton(UIBarButtonItem?, animated: Bool)](uinavigationitem/setleftbarbutton(_:animated:).md)
  Sets the custom bar button item, optionally animating the transition to the new item.
- [func setRightBarButtonItems([UIBarButtonItem]?, animated: Bool)](uinavigationitem/setrightbarbuttonitems(_:animated:).md)
  Sets the right bar button items, optionally animating the transition to the new items.
- [func setRightBarButton(UIBarButtonItem?, animated: Bool)](uinavigationitem/setrightbarbutton(_:animated:).md)
  Sets the custom bar button item, optionally animating the transition to the view.
### Getting and setting properties
- [var prompt: String?](uinavigationitem/prompt.md)
  A single line of text that displays at the top of the navigation bar.
- [var leftItemsSupplementBackButton: Bool](uinavigationitem/leftitemssupplementbackbutton.md)
  A Boolean value that indicates whether the left items display in addition to the Back button.
### Overriding the navigation bar’s appearance settings
- [var standardAppearance: UINavigationBarAppearance?](uinavigationitem/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](uinavigationitem/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](uinavigationitem/scrolledgeappearance.md)
  The appearance settings for a standard-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](uinavigationitem/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
### Integrating search into your interface
- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.
### Supporting navigation bar customization
- [var customizationIdentifier: String?](uinavigationitem/customizationidentifier.md)
  A globally unique string that enables user customization of the navigation bar layout.
### Working with the overflow menu
- [var additionalOverflowItems: UIDeferredMenuElement?](uinavigationitem/additionaloverflowitems.md)
  Additional items to present in the overflow menu.
- [var overflowPresentationSource: (any UIPopoverPresentationControllerSourceItem)?](uinavigationitem/overflowpresentationsource.md)
  The item you can use as an anchor to present a custom UI from the overflow menu button.
### Customizing the title menu
- [var titleMenuProvider: (([UIMenuElement]) -> UIMenu?)?](uinavigationitem/titlemenuprovider.md)
  A closure that generates the navigation item’s title menu.
- [var documentProperties: UIDocumentProperties?](uinavigationitem/documentproperties.md)
  An object that provides the document header for the title menu.
- [class UIDocumentProperties](uidocumentproperties.md)
  Information that UIKit uses to generate a document header for a navigation item’s title menu.
### Renaming documents
- [var renameDelegate: (any UINavigationItemRenameDelegate)?](uinavigationitem/renamedelegate-8jiuf.md)
  The delegate for renaming the navigation item.
- [protocol UINavigationItemRenameDelegate](uinavigationitemrenamedelegate-5j4ws.md)
  Methods an object implements to rename a navigation item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationController](uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
- [class UINavigationBar](uinavigationbar.md)
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [class UITabBarController](uitabbarcontroller.md)
  A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [class UITab](uitab.md)
  An object that manages a tab in a tab bar.
- [class UISearchTab](uisearchtab.md)
  A tab subclass that represents the system’s search tab.
- [class UITabGroup](uitabgroup.md)
  An object that manages a collection of tab objects.
- [class UIPageViewController](uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem)*