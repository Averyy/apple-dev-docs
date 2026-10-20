# isEditing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating if any editors are registered with the controller.

**Availability**:
- macOS

## Declaration

```swift
var isEditing: Bool { get }
```

```objc
@property (readonly, getter=isEditing) BOOL editing;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when an editor is registered with the controller object or [`false`](../../Swift/false.md) when no editor is registered.

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
- [func discardEditing()](./discardediting%28%29.md)
  Discards any pending changes by registered editors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroller/isediting)*