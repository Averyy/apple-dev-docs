# documentMenuWasCancelled(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user dismissed the document menu.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
optional func documentMenuWasCancelled(_ documentMenu: UIDocumentMenuViewController)
```

```objc
- (void) documentMenuWasCancelled:(UIDocumentMenuViewController *) documentMenu;
```

## Parameters

- `documentMenu`: The document menu object that called this method.

## See Also

### Responding to user actions
- [func documentMenu(UIDocumentMenuViewController, didPickDocumentPicker: UIDocumentPickerViewController)](./documentmenu%28_,didpickdocumentpicker%29.md)
  Tells the delegate that the user has selected a document picker from the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenuwascancelled(_:))*