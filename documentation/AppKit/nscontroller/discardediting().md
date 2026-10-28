# discardEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Discards any pending changes by registered editors.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func discardEditing()
```

```objc
- (void) discardEditing;
```

## Discussion

The receiver invokes [`discardEditing`](../../ObjectiveC/nsobject-swift.class/discardediting.md) on any current editors.

## See Also

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](./objectdidbeginediting%28_%29.md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](./objectdidendediting%28_%29.md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing() -> Bool](./commitediting%28%29.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempts to commit any pending changes in known editors of the receiver.
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/discardediting())*