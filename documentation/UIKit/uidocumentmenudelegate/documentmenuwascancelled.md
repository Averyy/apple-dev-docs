# documentMenuWasCancelled(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user dismissed the document menu.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func documentMenuWasCancelled(_ documentMenu: UIDocumentMenuViewController)
```

## Parameters

- `documentMenu`: The document menu object that called this method.

## See Also

- [func documentMenu(UIDocumentMenuViewController, didPickDocumentPicker: UIDocumentPickerViewController)](uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:).md)
  Tells the delegate that the user has selected a document picker from the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenuwascancelled(_:))*