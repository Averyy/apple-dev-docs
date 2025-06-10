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
- [static var inline: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.enum/inline.md)
  A constant that places the search bar on the trailing edge of the navigation bar, inline with the other content.
- [UINavigationItem.SearchBarPlacement.stacked](uinavigationitem/searchbarplacement-swift.enum/stacked.md)
  A constant that stacks the search bar vertically below the other content in the navigation bar.
### Enumeration Cases
- [UINavigationItem.SearchBarPlacement.integrated](uinavigationitem/searchbarplacement-swift.enum/integrated.md)
  The navigation bar will place the search bar inline with other content, on the trailing edge. On iPhone, when the navigation bar belongs to a UINavigationController, the search bar may be integrated into the toolbar.
- [UINavigationItem.SearchBarPlacement.integratedButton](uinavigationitem/searchbarplacement-swift.enum/integratedbutton.md)
  Placement is the same as Integrated, except that the inactive search bar is always shown as a button even when space permits a search field.
- [UINavigationItem.SearchBarPlacement.integratedCentered](uinavigationitem/searchbarplacement-swift.enum/integratedcentered.md)
  Placement is the same as Integrated, except that in regular width on iPad, the search bar is centered in the navigation bar. Only respected when used in a view controller that is a descendant of a tab bar controller or when using a navigation item style that requires a leading aligned title
### Initializers
- [init?(rawValue: Int)](uinavigationitem/searchbarplacement-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var searchController: UISearchController?](uinavigationitem/searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var hidesSearchBarWhenScrolling: Bool](uinavigationitem/hidessearchbarwhenscrolling.md)
  A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
- [var preferredSearchBarPlacement: UINavigationItem.SearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)
  The preferred placement of the search bar in the navigation bar.
- [var searchBarPlacementAllowsExternalIntegration: Bool](uinavigationitem/searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementAllowsToolbarIntegration: Bool](uinavigationitem/searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.enum)*