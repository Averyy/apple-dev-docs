# objectDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to inform the receiver that `editor` has committed or discarded its changes.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func objectDidEndEditing(_ editor: any NSEditor)
```

```objc
- (void) objectDidEndEditing:(id<NSEditor>) editor;
```

## See Also

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](./objectdidbeginediting%28_%29.md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func commitEditing() -> Bool](./commitediting%28%29.md)
  Attempts to commit any pending edits.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](./discardediting%28%29.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/objectdidendediting(_:))*