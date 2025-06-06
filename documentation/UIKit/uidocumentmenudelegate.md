# UIDocumentMenuDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods that you must implement to track user interactions with a document menu view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol UIDocumentMenuDelegate : NSObjectProtocol
```

#### Overview

The document menu calls the methods of this protocol when the user selects a document picker or dismisses the menu. If the user selects a document picker, set the picker’s delegate and present it.

## Topics

### Responding to user actions
- [func documentMenu(UIDocumentMenuViewController, didPickDocumentPicker: UIDocumentPickerViewController)](uidocumentmenudelegate/documentmenu(_:didpickdocumentpicker:).md)
  Tells the delegate that the user has selected a document picker from the menu.
- [func documentMenuWasCancelled(UIDocumentMenuViewController)](uidocumentmenudelegate/documentmenuwascancelled(_:).md)
  Tells the delegate that the user dismissed the document menu.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIDocumentMenuDelegate)?](uidocumentmenuviewcontroller/delegate.md)
  The document menu’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate)*