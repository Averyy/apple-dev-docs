# presentOptionsMenu(from:in:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays an options menu and anchors it to the specified location in the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func presentOptionsMenu(from rect: CGRect, in view: UIView, animated: Bool) -> Bool
```

```objc
- (BOOL) presentOptionsMenuFromRect:(CGRect) rect inView:(UIView *) view animated:(BOOL) animated;
```

#### Return Value

[`true`](../../Swift/true.md) if the options menu was displayed or [`false`](../../Swift/false.md) if it was not. The options menu may not be displayed in cases where there are no appropriate items to include in the menu.

#### Discussion

The contents of the options menu are built dynamically based on three things:

- The type of the document (as specified by the [`uti`](./uti.md) property)
- The set of installed apps that have registered support for opening documents
- The actions that you have indicated as supported in the document interaction controller delegate’s [`documentInteractionController(_:canPerformAction:)`](../uidocumentinteractioncontrollerdelegate/documentinteractioncontroller%28_,canperformaction%29.md) method

Options that cannot be performed on the current document are not included in the menu. For example, if the document cannot be opened by any known apps, the menu does not include options for opening it.

This method displays the options menu asynchronously. The menu is dismissed automatically when the user selects one of the available options. You can also dismiss it programmatically using the [`dismissMenu(animated:)`](./dismissmenu%28animated%29.md) method.

To instead present a menu that contains only a list of apps capable of opening the current document, the [`presentOpenInMenu(from:in:animated:)`](./presentopeninmenu%28from,in,animated%29.md) method instead.

## Parameters

- `rect`: The location (in the coordinate system of `view`) at which to anchor the menu.
- `view`: The view from which to display the options menu.
- `animated`: Specify [`true`](../../Swift/true.md) to animate the appearance of the menu or [`false`](../../Swift/false.md) to display it immediately.

## See Also

### Presenting and dismissing menus
- [func presentOptionsMenu(from: UIBarButtonItem, animated: Bool) -> Bool](./presentoptionsmenu%28from,animated%29.md)
  Displays an options menu and anchors it to the specified bar button item.
- [func presentOpenInMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](./presentopeninmenu%28from,in,animated%29.md)
  Displays a menu for opening the document and anchors that menu to the specified view.
- [func presentOpenInMenu(from: UIBarButtonItem, animated: Bool) -> Bool](./presentopeninmenu%28from,animated%29.md)
  Displays a menu for opening the document and anchors that menu to the specified bar button item.
- [func dismissMenu(animated: Bool)](./dismissmenu%28animated%29.md)
  Dismisses the currently active menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:))*