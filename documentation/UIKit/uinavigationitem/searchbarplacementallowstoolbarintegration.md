# searchBarPlacementAllowsToolbarIntegration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var searchBarPlacementAllowsToolbarIntegration: Bool { get set }
```

```objc
@property (nonatomic) BOOL searchBarPlacementAllowsToolbarIntegration;
```

## Overview

Defaults to [`true`](../../Swift/true.md). Set to [`false`](../../Swift/false.md) to prevent the system from placing the search bar among other [`UIToolbar`](../uitoolbar.md) items on iPhone.

## See Also

### Integrating search into your interface
- [var searchController: UISearchController?](./searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](./hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](./searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](./preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](./searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.
- [var searchBarPlacementAllowsExternalIntegration: Bool](./searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](./searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacementallowstoolbarintegration)*