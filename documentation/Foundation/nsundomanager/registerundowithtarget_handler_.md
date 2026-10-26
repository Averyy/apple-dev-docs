# registerUndoWithTarget:handler:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Records a single undo operation for a given target so that when the manager performs an undo, it executes the specified block.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) registerUndoWithTarget:(id) target handler:(void (^)(id)) undoHandler;
```

## Parameters

- `target`: The target of the undo operation.
- `undoHandler`: A block to be executed when an operation is undone.

  The block takes a single argument, the target of the undo operation.

## See Also

### Registering undo operations
- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](../undomanager/registerundo%28withtarget,selector,object%29.md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.
- [func prepare(withInvocationTarget: Any) -> Any](../undomanager/prepare%28withinvocationtarget%29.md)
  Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsundomanager/registerundowithtarget:handler:)*