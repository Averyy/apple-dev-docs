# setHidesBackButton(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Hides or shows the Back button, optionally animating the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setHidesBackButton(_ hidesBackButton: Bool, animated: Bool)
```

```objc
- (void) setHidesBackButton:(BOOL) hidesBackButton animated:(BOOL) animated;
```

## Parameters

- `hidesBackButton`: Specify [`true`](../../Swift/true.md) if the Back button should be hidden when this navigation item is the top item. Specify [`false`](../../Swift/false.md) if the Back button should be visible, assuming it hasn’t been replaced by a custom item.
- `animated`: [`true`](../../Swift/true.md) to animate the transition; otherwise, [`false`](../../Swift/false.md).

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
- [var hidesBackButton: Bool](./hidesbackbutton.md)
  A Boolean value that determines whether the navigation item hides the Back button.
- [var backAction: UIAction?](./backaction.md)
  The back action for the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/sethidesbackbutton(_:animated:))*