# UINavigationItem.BackButtonDisplayMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the display modes of the Back button.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum BackButtonDisplayMode
```

```c
enum UINavigationItemBackButtonDisplayMode : NSInteger;
```

## Topics

### Constants
- [UINavigationItem.BackButtonDisplayMode.default](./backbuttondisplaymode-swift.enum/default.md)
  The navigation item attempts to display a specific title, a generic title, or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.generic](./backbuttondisplaymode-swift.enum/generic.md)
  The navigation item attempts to display a generic title or no title for the Back button, depending on the space available.
- [UINavigationItem.BackButtonDisplayMode.minimal](./backbuttondisplaymode-swift.enum/minimal.md)
  The navigation item displays the Back button indicator instead of a title.
### Initializers
- [init?(rawValue: Int)](./backbuttondisplaymode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Back button
- [var backBarButtonItem: UIBarButtonItem?](./backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](./backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](./backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [var hidesBackButton: Bool](./hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](./sethidesbackbutton%28_,animated%29.md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](./backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.enum)*