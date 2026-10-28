# undoManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that the document uses to support undo/redo operations.

**Availability**:
- macOS

## Declaration

```swift
var undoManager: UndoManager? { get set }
```

```objc
@property (strong, nullable) NSUndoManager * undoManager;
```

## Discussion

When the [`hasUndoManager`](./hasundomanager.md) property is [`true`](../../Swift/true.md), accessing this property creates an [`UndoManager`](../../Foundation/undomanager.md) before returning it. If the [`hasUndoManager`](./hasundomanager.md) property is [`false`](../../Swift/false.md), the value of this property is `nil` by default. Assigning an undo manager to this property stores a reference to the object and automatically changes the [`hasUndoManager`](./hasundomanager.md) property to [`true`](../../Swift/true.md).

Whether you assign an undo manager or let the document create one, the document registers itself as an observer of various  [`UndoManager`](../../Foundation/undomanager.md) notifications so that appropriate document actions are stored on the undo stack.

## See Also

### Managing Undo and Redo Actions
- [var hasUndoManager: Bool](./hasundomanager.md)
  A Boolean value that indicates whether the document owns an undo manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/undomanager)*