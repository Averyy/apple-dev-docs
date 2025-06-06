# representativeItem

**Framework**: UIKit  
**Kind**: property

The item to display for a group when space is constrained.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var representativeItem: UIBarButtonItem? { get set }
```

#### Discussion

When space is constrained on the bar, UIKit may display a group’s representative item in place of its actual items. The representative item is a single bar button item that’s unique from the other items in the group. Tapping the representative item calls its action method normally. If you omit that action method, UIKit responds by automatically displaying the group’s items in a standard interface.

If you don’t specify a representative item for a group, UIKit tries to display the group’s items in the bar. If space is still constrained, UIKit may modify the appearance of items in the group to make room for all of the items. For example, UIKit may truncate the titles of textual bar button items. When space is severely constrained, UIKit may not even display a group’s representative item.

## See Also

- [var barButtonItems: [UIBarButtonItem]](uibarbuttonitemgroup/barbuttonitems.md)
  The bar button items to display on the bar.
- [var alwaysAvailable: Bool](uibarbuttonitemgroup/alwaysavailable.md)
  A Boolean value that determines whether the group is always available through the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/representativeitem)*