# discardEditing()

**Framework**: AppKit  
**Kind**: method

Discards any pending changes by registered editors.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func discardEditing()
```

#### Discussion

The receiver invokes [`discardEditing`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/discardEditing) on any current editors.

## See Also

- [func objectDidBeginEditing(any NSEditor)](nscontroller/objectdidbeginediting(_:).md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](nscontroller/objectdidendediting(_:).md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nscontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempts to commit any pending changes in known editors of the receiver.
- [var isEditing: Bool](nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/discardediting())*