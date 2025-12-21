# isEditing

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating if any editors are registered with the controller.

**Availability**:
- macOS ?+

## Declaration

```swift
var isEditing: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when an editor is registered with the controller object or [`false`](https://developer.apple.com/documentation/Swift/false) when no editor is registered.

## See Also

- [func objectDidBeginEditing(any NSEditor)](nscontroller/objectdidbeginediting(_:).md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](nscontroller/objectdidendediting(_:).md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nscontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](nscontroller/discardediting.md)
  Discards any pending changes by registered editors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/isediting)*