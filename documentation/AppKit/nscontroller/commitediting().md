# commitEditing()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to commit any pending edits.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func commitEditing() -> Bool
```

```objc
- (BOOL) commitEditing;
```

#### Return Value

[`true`](../../Swift/true.md) if successful or no edits were pending.

#### Discussion

The receiver invokes [`commitEditing`](../../ObjectiveC/nsobject-swift.class/commitediting.md) on any current editors, returning their response. A commit is denied if the receiver fails to apply the changes to the model object, perhaps due to a validation error.

## See Also

### Managing editing
- [func objectDidBeginEditing(any NSEditor)](./objectdidbeginediting%28_%29.md)
  Invoked to inform the receiver that `editor` has uncommitted changes that can affect the receiver.
- [func objectDidEndEditing(any NSEditor)](./objectdidendediting%28_%29.md)
  Invoked to inform the receiver that `editor` has committed or discarded its changes.
- [func commitEditing(withDelegate: Any?, didCommit: Selector?, contextInfo: UnsafeMutableRawPointer?)](./commitediting%28withdelegate,didcommit,contextinfo%29.md)
  Attempts to commit any pending changes in known editors of the receiver.
- [func discardEditing()](./discardediting%28%29.md)
  Discards any pending changes by registered editors.
- [var isEditing: Bool](./isediting.md)
  A Boolean value indicating if any editors are registered with the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/commitediting())*