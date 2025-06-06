# UINavigationItem.SearchBarPlacement

**Framework**: UIKit  
**Kind**: enum

Constants that determine where the search bar appears in the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum SearchBarPlacement
```

#### Overview

Use these constants to specify the placement of the search bar that belongs to the navigation item’s search controller ([`searchController`](uinavigationitem/searchcontroller.md)).

## Topics

### Constants
- [UINavigationItem.SearchBarPlacement.automatic](uinavigationitem/searchbarplacement-swift.enum/automatic.md)
  A constant that places the search bar according to the current layout.
- [UINavigationItem.SearchBarPlacement.inline](uinavigationitem/searchbarplacement-swift.enum/inline.md)
  A constant that places the search bar on the trailing edge of the navigation bar, inline with the other content.
- [UINavigationItem.SearchBarPlacement.stacked](uinavigationitem/searchbarplacement-swift.enum/stacked.md)
  A constant that stacks the search bar vertically below the other content in the navigation bar.
### Initializers
- [init?(rawValue: Int)](uinavigationitem/searchbarplacement-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.enum)*