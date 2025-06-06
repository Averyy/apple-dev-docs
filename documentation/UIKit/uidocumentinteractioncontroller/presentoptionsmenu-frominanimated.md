# presentOptionsMenu(from:in:animated:)

**Framework**: UIKit  
**Kind**: method

Displays an options menu and anchors it to the specified location in the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentOptionsMenu(from rect: CGRect, in view: UIView, animated: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the options menu was displayed or [`false`](https://developer.apple.com/documentation/swift/false) if it was not. The options menu may not be displayed in cases where there are no appropriate items to include in the menu.

#### Discussion

The contents of the options menu are built dynamically based on three things:

- The type of the document (as specified by the [`uti`](uidocumentinteractioncontroller/uti.md) property)
- The set of installed apps that have registered support for opening documents
- The actions that you have indicated as supported in the document interaction controller delegate’s [`documentInteractionController(_:canPerformAction:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:).md) method

Options that cannot be performed on the current document are not included in the menu. For example, if the document cannot be opened by any known apps, the menu does not include options for opening it.

This method displays the options menu asynchronously. The menu is dismissed automatically when the user selects one of the available options. You can also dismiss it programmatically using the [`dismissMenu(animated:)`](uidocumentinteractioncontroller/dismissmenu(animated:).md) method.

To instead present a menu that contains only a list of apps capable of opening the current document, the [`presentOpenInMenu(from:in:animated:)`](uidocumentinteractioncontroller/presentopeninmenu(from:in:animated:).md) method instead.

## Parameters

- `rect`: The location (in the coordinate system of  ) at which to anchor the menu.
- `view`: The view from which to display the options menu.
- `animated`: Specify   to animate the appearance of the menu or   to display it immediately.

## See Also

- [func presentOptionsMenu(from: UIBarButtonItem, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentoptionsmenu(from:animated:).md)
  Displays an options menu and anchors it to the specified bar button item.
- [func presentOpenInMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentopeninmenu(from:in:animated:).md)
  Displays a menu for opening the document and anchors that menu to the specified view.
- [func presentOpenInMenu(from: UIBarButtonItem, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentopeninmenu(from:animated:).md)
  Displays a menu for opening the document and anchors that menu to the specified bar button item.
- [func dismissMenu(animated: Bool)](uidocumentinteractioncontroller/dismissmenu(animated:).md)
  Dismisses the currently active menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:))*