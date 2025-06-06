# undoManager

**Framework**: AppKit  
**Kind**: property

The object that the document uses to support undo/redo operations.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var undoManager: UndoManager? { get set }
```

#### Discussion

When the [`hasUndoManager`](nsdocument/hasundomanager.md) property is [`true`](https://developer.apple.com/documentation/swift/true), accessing this property creates an [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) before returning it. If the [`hasUndoManager`](nsdocument/hasundomanager.md) property is [`false`](https://developer.apple.com/documentation/swift/false), the value of this property is `nil` by default. Assigning an undo manager to this property stores a reference to the object and automatically changes the [`hasUndoManager`](nsdocument/hasundomanager.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

Whether you assign an undo manager or let the document create one, the document registers itself as an observer of various  [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) notifications so that appropriate document actions are stored on the undo stack.

## See Also

- [var hasUndoManager: Bool](nsdocument/hasundomanager.md)
  A Boolean value that indicates whether the document owns an undo manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/undomanager)*