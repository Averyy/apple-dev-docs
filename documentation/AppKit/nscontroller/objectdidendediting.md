# objectDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Invoked to inform the receiver that `editor` has committed or discarded its changes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func objectDidEndEditing(_ editor: any NSEditor)
```

## See Also

- [func objectDidBeginEditing(any NSEditor)](nscontroller/objectdidbeginediting(_:).md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Causes the receiver to attempt to commit any pending edits, returning [`true`](https://developer.apple.com/documentation/swift/true) if successful or no edits were pending.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nscontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](nscontroller/discardediting.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/objectdidendediting(_:))*