# runModal()

**Framework**: Collaboration  
**Kind**: method  
**Role**: Instance Method

Runs the receiver as an application-modal dialog.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal() -> Int
```

```objc
- (NSInteger) runModal;
```

## Return Value

`NSOKButton` if the user selected OK; otherwise,  `NSCancelButton`.

## Discussion

The receiver may create identities for selected records if necessary.

## See Also

### Running an Identity Picker
- [func runModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the receiver modally as a sheet attached to a specified window.
- [func runModal(for: NSWindow, completionHandler: ((NSApplication.ModalResponse) -> Void)?)](./runmodal%28for,completionhandler%29.md)
  Runs the identity picker modally as a sheet attached to a specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/runmodal())*