# UIDocumentMenuDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that you must implement to track user interactions with a document menu view controller.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](./uidocumentmenuviewcontroller.md).

## Declaration

```swift
@MainActor
protocol UIDocumentMenuDelegate : NSObjectProtocol
```

```objc
@protocol UIDocumentMenuDelegate <NSObject>
```

## Overview

The document menu calls the methods of this protocol when the user selects a document picker or dismisses the menu. If the user selects a document picker, set the picker’s delegate and present it.

## Topics

### Responding to user actions
- [func documentMenu(UIDocumentMenuViewController, didPickDocumentPicker: UIDocumentPickerViewController)](./uidocumentmenudelegate/documentmenu%28_,didpickdocumentpicker%29.md)
  Tells the delegate that the user has selected a document picker from the menu.
- [func documentMenuWasCancelled(UIDocumentMenuViewController)](./uidocumentmenudelegate/documentmenuwascancelled%28_%29.md)
  Tells the delegate that the user dismissed the document menu.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the user-selected document picker
- [var delegate: (any UIDocumentMenuDelegate)?](./uidocumentmenuviewcontroller/delegate.md)
  The document menu’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenudelegate)*