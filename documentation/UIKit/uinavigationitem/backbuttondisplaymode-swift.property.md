# backButtonDisplayMode

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The display mode of the Back button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode { get set }
```

```objc
@property (nonatomic, assign, readwrite) UINavigationItemBackButtonDisplayMode backButtonDisplayMode;
```

#### Discussion

When the `backBarButtonItem` property is `nil`, the navigation item uses this display mode to determine the title of its Back button. The default value of this property is [`UINavigationItem.BackButtonDisplayMode.default`](./backbuttondisplaymode-swift.enum/default.md).

## See Also

### Configuring the Back button
- [var backBarButtonItem: UIBarButtonItem?](./backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](./backbuttontitle.md)
  The custom title of the Back button.
- [UINavigationItem.BackButtonDisplayMode](./backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [var hidesBackButton: Bool](./hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](./sethidesbackbutton%28_,animated%29.md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](./backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/backbuttondisplaymode-swift.property)*