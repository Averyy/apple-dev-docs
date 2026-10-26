# INUIAddVoiceShortcutButtonDelegate

**Framework**: IntentsUI  
**Kind**: protocol  
**Role**: Protocol

The protocol an object implements to receive notifications from the Siri Shortcut button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol INUIAddVoiceShortcutButtonDelegate : NSObjectProtocol
```

```objc
@protocol INUIAddVoiceShortcutButtonDelegate <NSObject>
```

## Topics

### Presenting Shortcut Editors
- [func present(INUIAddVoiceShortcutViewController, for: INUIAddVoiceShortcutButton)](./inuiaddvoiceshortcutbuttondelegate/present%28_,for%29-5foo8.md)
  Tells the delegate to present the *Add Shortcut* view controller.
- [func present(INUIEditVoiceShortcutViewController, for: INUIAddVoiceShortcutButton)](./inuiaddvoiceshortcutbuttondelegate/present%28_,for%29-9n4m9.md)
  Tells the delegate to present the *Edit Shortcut* view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Presenting Shortcut Editors
- [var shortcut: INShortcut?](./inuiaddvoiceshortcutbutton/shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.
- [var delegate: (any INUIAddVoiceShortcutButtonDelegate)?](./inuiaddvoiceshortcutbutton/delegate.md)
  The object that receives presentation requests from the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutbuttondelegate)*