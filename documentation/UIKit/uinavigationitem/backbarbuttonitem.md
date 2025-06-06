# backBarButtonItem

**Framework**: UIKit  
**Kind**: property

The bar button item for adding a Back button to the navigation bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var backBarButtonItem: UIBarButtonItem? { get set }
```

#### Discussion

When this navigation item is immediately below the top item in the stack, the navigation controller derives the Back button for the navigation bar from this navigation item. If you want to specify a custom title or image for the Back button, you can assign a custom bar button item (with your custom title or image) to this property. When you configure your bar button item, don’t assign a custom view to it; the navigation item ignores custom views in the [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md).

When this property is `nil`, the navigation item determines the title of its Back button according to its [`backButtonDisplayMode`](uinavigationitem/backbuttondisplaymode-swift.property.md). The default value of this property is `nil`.

## See Also

- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.
- [var backButtonTitle: String?](uinavigationitem/backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [var hidesBackButton: Bool](uinavigationitem/hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](uinavigationitem/sethidesbackbutton(_:animated:).md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](uinavigationitem/backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbarbuttonitem)*