# alwaysAvailable

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the group is always available through the UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var alwaysAvailable: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to ensure that the functionality in this group is available to people regardless of the customization of the groups.

When the value is [`true`](https://developer.apple.com/documentation/Swift/true), UIKit places the items in this group in the overflow menu for the [`UIUserInterfaceIdiom.phone`](uiuserinterfaceidiom/phone.md) and [`UIUserInterfaceIdiom.pad`](uiuserinterfaceidiom/pad.md) idioms. This property doesn’t have an effect for the [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) idiom.

## See Also

- [var barButtonItems: [UIBarButtonItem]](uibarbuttonitemgroup/barbuttonitems.md)
  The bar button items to display on the bar.
- [var representativeItem: UIBarButtonItem?](uibarbuttonitemgroup/representativeitem.md)
  The item to display for a group when space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/alwaysavailable)*