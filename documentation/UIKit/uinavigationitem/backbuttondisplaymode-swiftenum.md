# UINavigationItem.BackButtonDisplayMode

**Framework**: UIKit  
**Kind**: enum

Constants that describe the display modes of the Back button.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum BackButtonDisplayMode
```

## Topics

### Constants
- [UINavigationItem.BackButtonDisplayMode.default](uinavigationitem/backbuttondisplaymode-swift.enum/default.md)
  The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.generic](uinavigationitem/backbuttondisplaymode-swift.enum/generic.md)
  The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.minimal](uinavigationitem/backbuttondisplaymode-swift.enum/minimal.md)
  The navigation item displays the Back button indicator instead of a title.
### Initializers
- [init?(rawValue: Int)](uinavigationitem/backbuttondisplaymode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var backBarButtonItem: UIBarButtonItem?](uinavigationitem/backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](uinavigationitem/backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](uinavigationitem/backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [var hidesBackButton: Bool](uinavigationitem/hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](uinavigationitem/sethidesbackbutton(_:animated:).md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](uinavigationitem/backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum)*