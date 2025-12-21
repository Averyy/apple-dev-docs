# searchBarPlacementAllowsExternalIntegration

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
var searchBarPlacementAllowsExternalIntegration: Bool { get set }
```

#### Overview

Set this value to indicate whether an object at a higher scope may take the search bar and integrate it somewhere other than the navigation bar (or toolbar) directly associated with this navigation item. [`UISplitViewController`](uisplitviewcontroller.md) uses this to allow Mac-like placement of the search bar on iPad. Defaults to [`false`](https://developer.apple.com/documentation/Swift/false).

Set to [`true`](https://developer.apple.com/documentation/Swift/true) to allow the containing [`UISplitViewController`](uisplitviewcontroller.md) to place the search bar in the navigation bar for the trailingmost column independent of the column used for this view controller. Ignored when [`searchController`](uinavigationitem/searchcontroller.md) is `nil`, when [`searchBarPlacement`](uinavigationitem/searchbarplacement-swift.property.md) is [`UINavigationItem.SearchBarPlacement.stacked`](uinavigationitem/searchbarplacement-swift.enum/stacked.md), or when not contained in a [`UISplitViewController`](uisplitviewcontroller.md).

When the top view controller’s navigation item has this property set to [`true`](https://developer.apple.com/documentation/Swift/true) in more than one column at the same time, only one will be respected; the columns are checked in order of [`UISplitViewController.Column.inspector`](uisplitviewcontroller/column/inspector.md), [`UISplitViewController.Column.secondary`](uisplitviewcontroller/column/secondary.md), [`UISplitViewController.Column.supplementary`](uisplitviewcontroller/column/supplementary.md), [`UISplitViewController.Column.primary`](uisplitviewcontroller/column/primary.md). If the search bar has a scope bar, the scope bar will not be moved into a different column.

## See Also

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
- [var searchBarPlacementAllowsToolbarIntegration: Bool](uinavigationitem/searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementallowsexternalintegration)*