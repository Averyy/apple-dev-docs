# shortcut

**Framework**: IntentsUI  
**Kind**: property  
**Role**: Instance Property

The shortcut Siri invokes when the user speaks the invocation phrase.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var shortcut: INShortcut? { get set }
```

```objc
@property (nonatomic, strong, nullable) INShortcut * shortcut;
```

## See Also

### Presenting Shortcut Editors
- [var delegate: (any INUIAddVoiceShortcutButtonDelegate)?](./delegate.md)
  The object that receives presentation requests from the button.
- [protocol INUIAddVoiceShortcutButtonDelegate](../inuiaddvoiceshortcutbuttondelegate.md)
  The protocol an object implements to receive notifications from the Siri Shortcut button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutbutton/shortcut)*