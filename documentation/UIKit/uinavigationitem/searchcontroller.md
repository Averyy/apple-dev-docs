# searchController

**Framework**: UIKit  
**Kind**: property

The search controller to integrate into your navigation interface.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var searchController: UISearchController? { get set }
```

#### Discussion

When a view controller in your navigation interface supports search, assign the corresponding search controller to this property. The navigation controller integrates the search bar from your search controller into the navigation bar interface, presenting a single bar for both search and navigation. Use the [`hidesSearchBarWhenScrolling`](uinavigationitem/hidessearchbarwhenscrolling.md) property to control the visibility of the search bar when scrolling.

## See Also

- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum.md)
  Constants that determine where the search bar appears in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchcontroller)*