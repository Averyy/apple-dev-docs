# NSUserInterfaceValidations

**Framework**: AppKit  
**Kind**: protocol

A protocol that a custom class can adopt to manage the enabled state of a UI element.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSUserInterfaceValidations
```

#### Overview

The [`NSUserInterfaceValidations`](nsuserinterfacevalidations.md) protocol works with the [`NSValidatedUserInterfaceItem`](nsvalidateduserinterfaceitem.md) protocol to allow the target of a user interface element such as a menu item or a toolbar item to decide whether or not the user interface element should be enabled.

Your custom classes should adopt this protocol if an instance may be the target of a user interface element and need to conditionally enable or disable the element based on the current state of the instance. For more details, read [`User Interface Validation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/UIValidation.html#//apple_ref/doc/uid/10000040i).

## Topics

### Validating user interface items
- [func validateUserInterfaceItem(any NSValidatedUserInterfaceItem) -> Bool](nsuserinterfacevalidations/validateuserinterfaceitem(_:).md)
  Returns a Boolean value that indicates whether the sender should be enabled.

## Relationships

### Conforming Types
- [NSApplication](nsapplication.md)
- [NSButton](nsbutton.md)
- [NSColorPanel](nscolorpanel.md)
- [NSComboBox](nscombobox.md)
- [NSDocument](nsdocument.md)
- [NSDocumentController](nsdocumentcontroller.md)
- [NSFontPanel](nsfontpanel.md)
- [NSForm](nsform.md)
- [NSMatrix](nsmatrix.md)
- [NSOpenPanel](nsopenpanel.md)
- [NSOutlineView](nsoutlineview.md)
- [NSPanel](nspanel.md)
- [NSPersistentDocument](nspersistentdocument.md)
- [NSPopUpButton](nspopupbutton.md)
- [NSSavePanel](nssavepanel.md)
- [NSSearchField](nssearchfield.md)
- [NSSecureTextField](nssecuretextfield.md)
- [NSSplitViewController](nssplitviewcontroller.md)
- [NSStatusBarButton](nsstatusbarbutton.md)
- [NSTableView](nstableview.md)
- [NSTextField](nstextfield.md)
- [NSTextView](nstextview.md)
- [NSTokenField](nstokenfield.md)
- [NSWindow](nswindow.md)

## See Also

- [protocol NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)
  A protocol that a custom class can adopt to manage the automatic enablement of a UI control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations)*