# searchBarPlacementBarButtonItem

**Framework**: UIKit  
**Kind**: property

An item you use to control the placement of the search bar in a toolbar on iPhone.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
var searchBarPlacementBarButtonItem: UIBarButtonItem { get }
```

#### Overview

When [`searchBarPlacement`](uinavigationitem/searchbarplacement-swift.property.md) is `.integrated` or `.integratedButton` and a search controller is present, use this bar button item in the view controller’s [`toolbarItems`](uiviewcontroller/toolbaritems.md) to control the placement of the search bar among them when the search bar is appearing in the [`UIToolbar`](uitoolbar.md) on iPhone. Without this bar button item, the positioning for the search bar defaults to trailingmost for the [`UIToolbar`](uitoolbar.md) case.

The system ignores this bar button item during toolbar layout if [`searchController`](uinavigationitem/searchcontroller.md) is `nil`. [`UIBarButtonItemGroup`](uibarbuttonitemgroup.md) throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) when you include this bar button item in its initialization. [`UINavigationItem`](uinavigationitem.md) throws an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) when you include this bar button item in [`leftBarButtonItems`](uinavigationitem/leftbarbuttonitems.md) or [`rightBarButtonItems`](uinavigationitem/rightbarbuttonitems.md).

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
- [var searchBarPlacementAllowsExternalIntegration: Bool](uinavigationitem/searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementAllowsToolbarIntegration: Bool](uinavigationitem/searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementbarbuttonitem)*