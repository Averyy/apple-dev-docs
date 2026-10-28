# UINavigationItem.SearchBarPlacement

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UINavigationItemSearchBarPlacement : NSInteger;
```

## Overview

Use these constants to specify the placement of the search bar that belongs to the navigation item’s search controller ([`searchController`](./searchcontroller.md)).

## Topics

### Constants
- [UINavigationItem.SearchBarPlacement.automatic](./searchbarplacement-swift.enum/automatic.md)
  A constant that places the search bar according to the current layout.
- [UINavigationItem.SearchBarPlacement.stacked](./searchbarplacement-swift.enum/stacked.md)
  A constant that stacks the search bar vertically below the other content in the navigation bar.
- [static var inline: UINavigationItem.SearchBarPlacement](./searchbarplacement-swift.enum/inline.md)
  A constant that places the search bar on the trailing edge of the navigation bar, inline with the other content.
### Enumeration Cases
- [UINavigationItem.SearchBarPlacement.integrated](./searchbarplacement-swift.enum/integrated.md)
  The navigation bar will place the search bar inline with other content, on the trailing edge. On iPhone, when the navigation bar belongs to a UINavigationController, the search bar may be integrated into the toolbar.
- [UINavigationItem.SearchBarPlacement.integratedButton](./searchbarplacement-swift.enum/integratedbutton.md)
  Placement is the same as Integrated, except that the inactive search bar is always shown as a button even when space permits a search field.
- [UINavigationItem.SearchBarPlacement.integratedCentered](./searchbarplacement-swift.enum/integratedcentered.md)
  Placement is the same as Integrated, except that in regular width on iPad, the search bar is centered in the navigation bar. Only respected when used in a view controller that is a descendant of a tab bar controller or when using a navigation item style that requires a leading aligned title
### Initializers
- [init?(rawValue: Int)](./searchbarplacement-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var searchBarPlacementAllowsExternalIntegration: Bool](./searchbarplacementallowsexternalintegration.md)
  A Boolean value that indicates whether an alternate object may integrate the search bar somewhere other than the navigation bar or toolbar.
- [var searchBarPlacementAllowsToolbarIntegration: Bool](./searchbarplacementallowstoolbarintegration.md)
  A Boolean value that indicates whether the system can place the search bar among other toolbar items on iPhone.
- [var searchBarPlacementBarButtonItem: UIBarButtonItem](./searchbarplacementbarbuttonitem.md)
  An item you use to control the placement of the search bar in a toolbar on iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/searchbarplacement-swift.enum)*