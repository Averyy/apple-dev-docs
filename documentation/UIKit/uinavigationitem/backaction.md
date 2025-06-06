# backAction

**Framework**: UIKit  
**Kind**: property

The back action for the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var backAction: UIAction? { get set }
```

#### Discussion

If a back button already appears in the navigation bar, setting this property replaces its action without modifying its appearance. Otherwise, setting this property generates a back button with the image or title from the action you specify, unless you use the [`UINavigationItem.ItemStyle.editor`](uinavigationitem/itemstyle/editor.md) navigation style.

## See Also

- [var backBarButtonItem: UIBarButtonItem?](uinavigationitem/backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backaction)*