# windowWillReturnUndoManager(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window’s undo manager has been requested. Returns the appropriate undo manager for the window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
optional func windowWillReturnUndoManager(_ window: NSWindow) -> UndoManager?
```

#### Return Value

The appropriate undo manager for the specified window.

#### Discussion

If this method is not implemented by the delegate, the window creates an[`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) for `window`. Further, after a window creates its own undo manager, this method is never again called on the delegate.

## Parameters

- `window`: The window whose undo manager is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillreturnundomanager(_:))*