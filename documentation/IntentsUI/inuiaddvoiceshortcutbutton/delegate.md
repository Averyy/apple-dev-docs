# delegate

**Framework**: IntentsUI  
**Kind**: property  
**Role**: Instance Property

The object that receives presentation requests from the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any INUIAddVoiceShortcutButtonDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<INUIAddVoiceShortcutButtonDelegate> delegate;
```

## See Also

### Presenting Shortcut Editors
- [var shortcut: INShortcut?](./shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.
- [protocol INUIAddVoiceShortcutButtonDelegate](../inuiaddvoiceshortcutbuttondelegate.md)
  The protocol an object implements to receive notifications from the Siri Shortcut button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutbutton/delegate)*