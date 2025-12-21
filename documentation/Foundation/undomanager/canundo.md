# canUndo

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the manager has any actions to undo.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var canUndo: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the manager has any actions to undo, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

The return value doesn’t mean you can safely invoke [`undo()`](undomanager/undo().md) or [`undoNestedGroup()`](undomanager/undonestedgroup().md)—you may have to close open undo groups first.

## See Also

- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](undomanager/registerundo(withtarget:selector:object:).md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.
- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [var canRedo: Bool](undomanager/canredo.md)
  A Boolean value that indicates whether the manager has any actions to redo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/canundo)*