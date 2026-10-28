# hidesBackButton

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the navigation item hides the Back button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hidesBackButton: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL hidesBackButton;
```

## Discussion

When set to [`true`](../../Swift/true.md), the Back button is hidden when this navigation item is the top item. This is true regardless of the value in the [`leftItemsSupplementBackButton`](./leftitemssupplementbackbutton.md) property. When set to [`false`](../../Swift/false.md), the Back button is shown if it’s still present. (It can be replaced by values in either the [`leftBarButtonItem`](./leftbarbuttonitem.md) or [`leftBarButtonItems`](./leftbarbuttonitems.md) properties.) The default value is [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var backItem: UINavigationItem?](../uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.
### Configuring the Back button
- [var backBarButtonItem: UIBarButtonItem?](./backbarbuttonitem.md)
  The bar button item for adding a Back button to the navigation bar.
- [var backButtonTitle: String?](./backbuttontitle.md)
  The custom title of the Back button.
- [var backButtonDisplayMode: UINavigationItem.BackButtonDisplayMode](./backbuttondisplaymode-swift.property.md)
  The display mode of the Back button.
- [UINavigationItem.BackButtonDisplayMode](./backbuttondisplaymode-swift.enum.md)
  Constants that describe the display modes of the Back button.
- [func setHidesBackButton(Bool, animated: Bool)](./sethidesbackbutton%28_,animated%29.md)
  Hides or shows the Back button, optionally animating the transition.
- [var backAction: UIAction?](./backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/hidesbackbutton)*