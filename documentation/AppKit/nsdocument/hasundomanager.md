# hasUndoManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document owns an undo manager object.

**Availability**:
- macOS

## Declaration

```swift
var hasUndoManager: Bool { get set }
```

```objc
@property BOOL hasUndoManager;
```

#### Discussion

If you change the value of this property to NO and the document already owns an [`UndoManager`](../../Foundation/undomanager.md) object, the document removes the undo manager as an observer of undo-related notifications and then removes its reference to the object.

## See Also

### Managing Undo and Redo Actions
- [var undoManager: UndoManager?](./undomanager.md)
  The object that the document uses to support undo/redo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/hasundomanager)*