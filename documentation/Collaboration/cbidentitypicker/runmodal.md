# runModal()

**Framework**: Collaboration  
**Kind**: method

Runs the receiver as an application-modal dialog.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal() -> Int
```

#### Return Value

`NSOKButton` if the user selected OK; otherwise,  `NSCancelButton`.

#### Discussion

The receiver may create identities for selected records if necessary.

## See Also

- [func runModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](cbidentitypicker/runmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the receiver modally as a sheet attached to a specified window.
- [func runModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](cbidentitypicker/runmodal(for:completionhandler:).md)
  Runs the identity picker modally as a sheet attached to a specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/runmodal())*