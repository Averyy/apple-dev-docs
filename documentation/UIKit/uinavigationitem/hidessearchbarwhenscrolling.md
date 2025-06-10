# hidesSearchBarWhenScrolling

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hidesSearchBarWhenScrolling: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the search bar is visible only when the scroll position equals the top of your content view. When the user scrolls down, the search bar collapses into the navigation bar. Scrolling back to the top reveals the search bar again. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the search bar remains regardless of the current scroll position.

You must configure the [`searchController`](uinavigationitem/searchcontroller.md) property for this property to have any effect. The navigation controller hides and shows only the search bar provided by the search controller in that property.

## See Also

- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
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
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/hidessearchbarwhenscrolling)*