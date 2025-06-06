# runModal(for:modalDelegate:didEnd:contextInfo:)

**Framework**: Collaboration  
**Kind**: method

Runs the receiver modally as a sheet attached to a specified window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal(for window: NSWindow, modalDelegate delegate: Any?, didEnd didEndSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

The `didEndSelector` parameter is a selector that takes three arguments. The corresponding method should have a declaration modeled on the following example:

```objc
- (void)identityPickerDidEnd:(CBIdentityPicker *)identityPicker returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo;
```

where the `identityPicker` argument is the identity picker object, the `returnCode` argument  is the button the user clicked, and `contextInfo` is the same `contextInfo` argument that was passed in the original message.

## Parameters

- `window`: The parent window for the sheet.
- `delegate`: The delegate for the modal session.
- `didEndSelector`: A message sent to the delegate after the user responds but before the sheet is dismissed.
- `contextInfo`: Contextual data passed to the delegate in the   message.

## See Also

- [Identity Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004490)
- [func runModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](cbidentitypicker/runmodal(for:completionhandler:).md)
  Runs the identity picker modally as a sheet attached to a specified window.
- [func runModal() -> Int](cbidentitypicker/runmodal.md)
  Runs the receiver as an application-modal dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/runmodal(for:modaldelegate:didend:contextinfo:))*