# INUIAddVoiceShortcutViewControllerDelegate

**Framework**: IntentsUI  
**Kind**: protocol  
**Role**: Protocol

The protocol an object implements to receive notifications from the view controller adding a shortcut to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol INUIAddVoiceShortcutViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol INUIAddVoiceShortcutViewControllerDelegate <NSObject>
```

## Topics

### Handling View Controller Events
- [func addVoiceShortcutViewController(INUIAddVoiceShortcutViewController, didFinishWith: INVoiceShortcut?, error: (any Error)?)](./inuiaddvoiceshortcutviewcontrollerdelegate/addvoiceshortcutviewcontroller%28_,didfinishwith,error%29.md)
  Tells the delegate the view controller added the shortcut to Siri.
- [func addVoiceShortcutViewControllerDidCancel(INUIAddVoiceShortcutViewController)](./inuiaddvoiceshortcutviewcontrollerdelegate/addvoiceshortcutviewcontrollerdidcancel%28_%29.md)
  Tells the delegate the user canceled the add-to-Siri process.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling View Controller Events
- [var delegate: (any INUIAddVoiceShortcutViewControllerDelegate)?](./inuiaddvoiceshortcutviewcontroller/delegate.md)
  The object that retrieves notifications from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontrollerdelegate)*