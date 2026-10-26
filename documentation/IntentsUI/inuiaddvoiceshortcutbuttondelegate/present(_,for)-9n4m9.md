# present(_:for:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate to present the *Edit Shortcut* view controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func present(_ editVoiceShortcutViewController: INUIEditVoiceShortcutViewController, for addVoiceShortcutButton: INUIAddVoiceShortcutButton)
```

```objc
- (void) presentEditVoiceShortcutViewController:(INUIEditVoiceShortcutViewController *) editVoiceShortcutViewController forAddVoiceShortcutButton:(INUIAddVoiceShortcutButton *) addVoiceShortcutButton;
```

## Parameters

- `editVoiceShortcutViewController`: The view controller to present.
- `addVoiceShortcutButton`: The Siri Shortcut button calling this method.

## See Also

### Presenting Shortcut Editors
- [func present(INUIAddVoiceShortcutViewController, for: INUIAddVoiceShortcutButton)](./present%28_,for%29-5foo8.md)
  Tells the delegate to present the *Add Shortcut* view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutbuttondelegate/present(_:for:)-9n4m9)*