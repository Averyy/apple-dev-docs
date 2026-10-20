# hidesSearchBarWhenScrolling

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app hides the integrated search bar when scrolling any underlying content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hidesSearchBarWhenScrolling: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL hidesSearchBarWhenScrolling;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the search bar is visible only when the scroll position equals the top of your content view. When the user scrolls down, the search bar collapses into the navigation bar. Scrolling back to the top reveals the search bar again. When the value of this property is [`false`](../../Swift/false.md), the search bar remains regardless of the current scroll position.

You must configure the [`searchController`](./searchcontroller.md) property for this property to have any effect. The navigation controller hides and shows only the search bar provided by the search controller in that property.

## See Also

### Integrating search into your interface
- [var searchController: UISearchController?](./searchcontroller.md)
  The search controller to integrate into your navigation interface.
- [var searchBarPlacement: UINavigationItem.SearchBarPlacement](./searchbarplacement-swift.property.md)
  The placement of the search bar in the navigation bar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/hidessearchbarwhenscrolling)*