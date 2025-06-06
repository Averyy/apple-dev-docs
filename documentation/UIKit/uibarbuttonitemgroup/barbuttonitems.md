# barButtonItems

**Framework**: UIKit  
**Kind**: property

The bar button items to display on the bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var barButtonItems: [UIBarButtonItem] { get set }
```

#### Discussion

You may include any number of bar button items in a group, but you should keep the total number of items relatively small because of space considerations. The items in a group are typically related to each other, but need not be. The array must contain at least one item.

Items can belong to only one group at a time. If you specify an item that’s already in a group, UIKit removes the item from its previous group before assigning it to the current group.

## See Also

- [var representativeItem: UIBarButtonItem?](uibarbuttonitemgroup/representativeitem.md)
  The item to display for a group when space is constrained.
- [var alwaysAvailable: Bool](uibarbuttonitemgroup/alwaysavailable.md)
  A Boolean value that determines whether the group is always available through the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/barbuttonitems)*