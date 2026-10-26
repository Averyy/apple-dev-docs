# editVoiceShortcutViewController(_:didUpdate:error:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate the user updated the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func editVoiceShortcutViewController(_ controller: INUIEditVoiceShortcutViewController, didUpdate voiceShortcut: INVoiceShortcut?, error: (any Error)?)
```

```objc
- (void) editVoiceShortcutViewController:(INUIEditVoiceShortcutViewController *) controller didUpdateVoiceShortcut:(INVoiceShortcut *) voiceShortcut error:(NSError *) error;
```

#### Discussion

The system calls this method after the user re-records the invocation phrase for the shortcut. If your app displays the phrase, the app should update its screen to show the new phrase by retrieving the phrase text from the [`invocationPhrase`](https://developer.apple.com/documentation/intents/invoiceshortcut/invocationphrase) property on voiceShortcut.

## Parameters

- `controller`: The view controller calling this method.
- `voiceShortcut`: The updated shortcut; otherwise, `nil` when an error occurred updating the shortcut.
- `error`: A error object when an error occurred updating the shortcut; otherwise, `nil`.

## See Also

### Handling Shortcut Changes
- [func editVoiceShortcutViewController(INUIEditVoiceShortcutViewController, didDeleteVoiceShortcutWithIdentifier: UUID)](./editvoiceshortcutviewcontroller%28_,diddeletevoiceshortcutwithidentifier%29.md)
  Tells the delegate the user deleted the shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuieditvoiceshortcutviewcontrollerdelegate/editvoiceshortcutviewcontroller(_:didupdate:error:))*