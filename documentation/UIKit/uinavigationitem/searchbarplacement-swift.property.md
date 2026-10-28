# searchBarPlacement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The placement of the search bar in the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var searchBarPlacement: UINavigationItem.SearchBarPlacement { get }
```

```objc
@property (nonatomic, assign, readonly) UINavigationItemSearchBarPlacement searchBarPlacement;
```

## Discussion

Use this property to determine the actual search bar placement when the [`preferredSearchBarPlacement`](./preferredsearchbarplacement.md) is [`UINavigationItem.SearchBarPlacement.automatic`](./searchbarplacement-swift.enum/automatic.md).

This property only applies when the navigation item has a [`searchController`](./searchcontroller.md).

## See Also

### Integrating search into your interface
- [var searchController: UISearchController?](./searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](./hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](./preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](./searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.
- [var searchBarPlacementAllowsExternalIntegration: Bool](./searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementAllowsToolbarIntegration: Bool](./searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](./searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.property)*