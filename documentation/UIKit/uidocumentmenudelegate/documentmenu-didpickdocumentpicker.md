# documentMenu(_:didPickDocumentPicker:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the user has selected a document picker from the menu.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func documentMenu(_ documentMenu: UIDocumentMenuViewController, didPickDocumentPicker documentPicker: UIDocumentPickerViewController)
```

#### Discussion

The document menu calls this method when the user selects a document picker. Set the document picker’s delegate, and then present it.

## Parameters

- `documentMenu`: The document menu object that called this method.
- `documentPicker`: The document picker that the user selected.

## See Also

- [func documentMenuWasCancelled(UIDocumentMenuViewController)](uidocumentmenudelegate/documentmenuwascancelled(_:).md)
  Tells the delegate that the user dismissed the document menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:))*