# INUIEditVoiceShortcutViewControllerDelegate

**Framework**: IntentsUI  
**Kind**: protocol  
**Role**: Protocol

The protocol an object implements to receive notifications from the view controller that edits or removes a shortcut in Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol INUIEditVoiceShortcutViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol INUIEditVoiceShortcutViewControllerDelegate <NSObject>
```

## Topics

### Handling Shortcut Changes
- [func editVoiceShortcutViewController(INUIEditVoiceShortcutViewController, didUpdate: INVoiceShortcut?, error: (any Error)?)](./inuieditvoiceshortcutviewcontrollerdelegate/editvoiceshortcutviewcontroller%28_,didupdate,error%29.md)
  Tells the delegate the user updated the shortcut.
- [func editVoiceShortcutViewController(INUIEditVoiceShortcutViewController, didDeleteVoiceShortcutWithIdentifier: UUID)](./inuieditvoiceshortcutviewcontrollerdelegate/editvoiceshortcutviewcontroller%28_,diddeletevoiceshortcutwithidentifier%29.md)
  Tells the delegate the user deleted the shortcut.
### Handling View Controller Events
- [func editVoiceShortcutViewControllerDidCancel(INUIEditVoiceShortcutViewController)](./inuieditvoiceshortcutviewcontrollerdelegate/editvoiceshortcutviewcontrollerdidcancel%28_%29.md)
  Tells the delegate the user canceled the edit-or-remove-shortcut process.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling View Controller Events
- [var delegate: (any INUIEditVoiceShortcutViewControllerDelegate)?](./inuieditvoiceshortcutviewcontroller/delegate.md)
  The object that retrieves notifications from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuieditvoiceshortcutviewcontrollerdelegate)*