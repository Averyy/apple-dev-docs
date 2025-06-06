# preferredSearchBarPlacement

**Framework**: UIKit  
**Kind**: property

The preferred placement of the search bar in the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Use this property to specify the search bar placement. If the value of the property is [`UINavigationItem.SearchBarPlacement.automatic`](uinavigationitem/searchbarplacement-swift.enum/automatic.md), use the [`searchBarPlacement`](uinavigationitem/searchbarplacement-swift.property.md) property to determine the actual placement. The default value of this property is [`UINavigationItem.SearchBarPlacement.automatic`](uinavigationitem/searchbarplacement-swift.enum/automatic.md).

This property only applies when the navigation item has a [`searchController`](uinavigationitem/searchcontroller.md).

## See Also

- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/preferredsearchbarplacement)*