# addVoiceShortcutViewController(_:didFinishWith:error:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate the view controller added the shortcut to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func addVoiceShortcutViewController(_ controller: INUIAddVoiceShortcutViewController, didFinishWith voiceShortcut: INVoiceShortcut?, error: (any Error)?)
```

```objc
- (void) addVoiceShortcutViewController:(INUIAddVoiceShortcutViewController *) controller didFinishWithVoiceShortcut:(INVoiceShortcut *) voiceShortcut error:(NSError *) error;
```

## Parameters

- `controller`: The view controller calling this method.
- `voiceShortcut`: The shortcut added to Siri. This parameter is `nil` when the controller isn’t able to add the shortcut to Siri.
- `error`: A error object if an error occurred adding the shortcut; otherwise, `nil`.

## See Also

### Handling View Controller Events
- [func addVoiceShortcutViewControllerDidCancel(INUIAddVoiceShortcutViewController)](./addvoiceshortcutviewcontrollerdidcancel%28_%29.md)
  Tells the delegate the user canceled the add-to-Siri process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontrollerdelegate/addvoiceshortcutviewcontroller(_:didfinishwith:error:))*