# documentMenu(_:didPickDocumentPicker:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the user has selected a document picker from the menu.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
func documentMenu(_ documentMenu: UIDocumentMenuViewController, didPickDocumentPicker documentPicker: UIDocumentPickerViewController)
```

```objc
- (void) documentMenu:(UIDocumentMenuViewController *) documentMenu didPickDocumentPicker:(UIDocumentPickerViewController *) documentPicker;
```

## Discussion

The document menu calls this method when the user selects a document picker. Set the document picker’s delegate, and then present it.

## Parameters

- `documentMenu`: The document menu object that called this method.
- `documentPicker`: The document picker that the user selected.

## See Also

### Responding to user actions
- [func documentMenuWasCancelled(UIDocumentMenuViewController)](./documentmenuwascancelled%28_%29.md)
  Tells the delegate that the user dismissed the document menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:))*