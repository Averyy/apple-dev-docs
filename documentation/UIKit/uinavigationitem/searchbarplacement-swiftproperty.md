# searchBarPlacement

**Framework**: UIKit  
**Kind**: property

The placement of the search bar in the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var searchBarPlacement: UINavigationItem.SearchBarPlacement { get }
```

#### Discussion

Use this property to determine the actual search bar placement when the [`preferredSearchBarPlacement`](uinavigationitem/preferredsearchbarplacement.md) is [`UINavigationItem.SearchBarPlacement.automatic`](uinavigationitem/searchbarplacement-swift.enum/automatic.md).

This property only applies when the navigation item has a [`searchController`](uinavigationitem/searchcontroller.md).

## See Also

- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.
- [var searchBarPlacementAllowsExternalIntegration: Bool](uinavigationitem/searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementAllowsToolbarIntegration: Bool](uinavigationitem/searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.property)*