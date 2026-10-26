# addVoiceShortcutViewControllerDidCancel(_:)

**Framework**: IntentsUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate the user canceled the add-to-Siri process.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func addVoiceShortcutViewControllerDidCancel(_ controller: INUIAddVoiceShortcutViewController)
```

```objc
- (void) addVoiceShortcutViewControllerDidCancel:(INUIAddVoiceShortcutViewController *) controller;
```

## Parameters

- `controller`: The view controller calling this method.

## See Also

### Handling View Controller Events
- [func addVoiceShortcutViewController(INUIAddVoiceShortcutViewController, didFinishWith: INVoiceShortcut?, error: (any Error)?)](./addvoiceshortcutviewcontroller%28_,didfinishwith,error%29.md)
  Tells the delegate the view controller added the shortcut to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontrollerdelegate/addvoiceshortcutviewcontrollerdidcancel(_:))*