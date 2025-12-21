# objectDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func objectDidBeginEditing(_ editor: any NSEditor)
```

## See Also

- [Cocoa Bindings Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html#//apple_ref/doc/uid/10000167i)
- [func objectDidEndEditing(any NSEditor)](nscontroller/objectdidendediting(_:).md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](nscontroller/commitediting.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](nscontroller/commitediting(withdelegate:didcommit:contextinfo:).md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](nscontroller/discardediting.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](nscontroller/isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/objectdidbeginediting(_:))*