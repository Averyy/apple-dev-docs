# searchBarPlacementAllowsToolbarIntegration

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var searchBarPlacementAllowsToolbarIntegration: Bool { get set }
```

#### Overview

Defaults to [`true`](https://developer.apple.com/documentation/swift/true). Set to [`false`](https://developer.apple.com/documentation/swift/false) to prevent the system from placing the search bar among other [`UIToolbar`](uitoolbar.md) items on iPhone.

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
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementallowstoolbarintegration)*