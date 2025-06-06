# hasUndoManager

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document owns an undo manager object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasUndoManager: Bool { get set }
```

#### Discussion

If you change the value of this property to NO and the document already owns an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object, the document removes the undo manager as an observer of undo-related notifications and then removes its reference to the object.

## See Also

- [var undoManager: UndoManager?](nsdocument/undomanager.md)
  The object that the document uses to support undo/redo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/hasundomanager)*