# dismissMenu(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the currently active menu.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dismissMenu(animated: Bool)
```

```objc
- (void) dismissMenuAnimated:(BOOL) animated;
```

## Discussion

Use this method to dismiss a menu programmatically. The document interaction controller can also dismiss the menu automatically in response to user actions.

## Parameters

- `animated`: Specify [`true`](../../Swift/true.md) to animate the dismissal of the currently active menu or [`false`](../../Swift/false.md) to dismiss it immediately.

## See Also

### Presenting and dismissing menus
- [func presentOptionsMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](./presentoptionsmenu%28from,in,animated%29.md)
  Displays an options menu and anchors it to the specified location in the view.
- [func presentOptionsMenu(from: UIBarButtonItem, animated: Bool) -> Bool](./presentoptionsmenu%28from,animated%29.md)
  Displays an options menu and anchors it to the specified bar button item.
- [func presentOpenInMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](./presentopeninmenu%28from,in,animated%29.md)
  Displays a menu for opening the document and anchors that menu to the specified view.
- [func presentOpenInMenu(from: UIBarButtonItem, animated: Bool) -> Bool](./presentopeninmenu%28from,animated%29.md)
  Displays a menu for opening the document and anchors that menu to the specified bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/dismissmenu(animated:))*