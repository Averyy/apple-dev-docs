# editVoiceShortcutViewController(_:didDeleteVoiceShortcutWithIdentifier:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate the user deleted the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func editVoiceShortcutViewController(_ controller: INUIEditVoiceShortcutViewController, didDeleteVoiceShortcutWithIdentifier deletedVoiceShortcutIdentifier: UUID)
```

```objc
- (void) editVoiceShortcutViewController:(INUIEditVoiceShortcutViewController *) controller didDeleteVoiceShortcutWithIdentifier:(NSUUID *) deletedVoiceShortcutIdentifier;
```

## Discussion

After the user deletes a shortcut, the shortcut is no longer available to Siri. Your app should reflect this change by displaying an [`INUIAddVoiceShortcutButton`](../inuiaddvoiceshortcutbutton.md) in the view for the action. The button lets the user know the action doesn’t have a shortcut, and provides the option to add one.

## Parameters

- `controller`: The view controller calling this method.
- `deletedVoiceShortcutIdentifier`: The identifier of the shortcut that the user deleted.

## See Also

### Handling Shortcut Changes
- [func editVoiceShortcutViewController(INUIEditVoiceShortcutViewController, didUpdate: INVoiceShortcut?, error: (any Error)?)](./editvoiceshortcutviewcontroller%28_,didupdate,error%29.md)
  Tells the delegate the user updated the shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuieditvoiceshortcutviewcontrollerdelegate/editvoiceshortcutviewcontroller(_:diddeletevoiceshortcutwithidentifier:))*