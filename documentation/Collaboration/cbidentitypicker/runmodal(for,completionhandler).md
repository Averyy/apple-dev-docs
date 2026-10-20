# runModal(for:completionHandler:)

**Framework**: Collaboration  
**Kind**: method  
**Role**: Instance Method

Runs the identity picker modally as a sheet attached to a specified window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func runModal(for window: NSWindow, completionHandler: (@Sendable (NSApplication.ModalResponse) -> Void)? = nil)
```

```swift
func runModal(for window: NSWindow) async -> NSApplication.ModalResponse
```

```objc
- (void) runModalForWindow:(NSWindow *) window completionHandler:(void (^)(NSModalResponse returnCode)) completionHandler;
```

## Parameters

- `window`: The parent window for the sheet.
- `completionHandler`: The handler to run after the return value is known, but before the sheet is dismissed.

## See Also

### Running an Identity Picker
- [func runModal(for: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the receiver modally as a sheet attached to a specified window.
- [func runModal() -> Int](./runmodal%28%29.md)
  Runs the receiver as an application-modal dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentitypicker/runmodal(for:completionhandler:))*