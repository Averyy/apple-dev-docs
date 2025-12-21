# hidesBackButton

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the navigation item hides the Back button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hidesBackButton: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/Swift/true), the Back button is hidden when this navigation item is the top item. This is true regardless of the value in the [`leftItemsSupplementBackButton`](uinavigationitem/leftitemssupplementbackbutton.md) property. When set to [`false`](https://developer.apple.com/documentation/Swift/false), the Back button is shown if it’s still present. (It can be replaced by values in either the [`leftBarButtonItem`](uinavigationitem/leftbarbuttonitem.md) or [`leftBarButtonItems`](uinavigationitem/leftbarbuttonitems.md) properties.) The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.
- [var backBarButtonItem: UIBarButtonItem?](uinavigationitem/backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](uinavigationitem/backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](uinavigationitem/sethidesbackbutton(_:animated:).md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](uinavigationitem/backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/hidesbackbutton)*