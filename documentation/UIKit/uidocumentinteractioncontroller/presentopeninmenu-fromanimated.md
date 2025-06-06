# presentOpenInMenu(from:animated:)

**Framework**: UIKit  
**Kind**: method

Displays a menu for opening the document and anchors that menu to the specified bar button item.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentOpenInMenu(from item: UIBarButtonItem, animated: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if this method was able to display the menu or [`false`](https://developer.apple.com/documentation/swift/false) if it was not.

#### Discussion

This method is similar to the [`presentOptionsMenu(from:animated:)`](uidocumentinteractioncontroller/presentoptionsmenu(from:animated:).md) method, but presents a menu restricted to a list of apps capable of opening the current document. This determination is made based on the document type (as indicated by the [`uti`](uidocumentinteractioncontroller/uti.md) property) and on the document types supported by the installed apps. To support one or more document types, an app must register those types in its `Info.plist` file using the `CFBundleDocumentTypes` key.

If there are no registered apps that support opening the document, the document interaction controller does not display a menu.

This method displays the menu asynchronously. The document interaction controller dismisses the menu automatically when the user selects an appropriate app. You can also dismiss it programmatically using the [`dismissMenu(animated:)`](uidocumentinteractioncontroller/dismissmenu(animated:).md) method.

## Parameters

- `item`: The bar button item to which to anchor the menu.
- `animated`: Specify   to animate the appearance of the menu or   to display it immediately.

## See Also

- [func presentOptionsMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:).md)
  Displays an options menu and anchors it to the specified location in the view.
- [func presentOptionsMenu(from: UIBarButtonItem, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentoptionsmenu(from:animated:).md)
  Displays an options menu and anchors it to the specified bar button item.
- [func presentOpenInMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentopeninmenu(from:in:animated:).md)
  Displays a menu for opening the document and anchors that menu to the specified view.
- [func dismissMenu(animated: Bool)](uidocumentinteractioncontroller/dismissmenu(animated:).md)
  Dismisses the currently active menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentopeninmenu(from:animated:))*