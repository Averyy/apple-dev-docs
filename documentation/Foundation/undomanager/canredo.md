# canRedo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the manager has any actions to redo.

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
var canRedo: Bool { get }
```

```objc
@property (readonly) BOOL canRedo;
```

## Discussion

[`true`](../../Swift/true.md) if the manager has any actions to redo, otherwise [`false`](../../Swift/false.md).

Because any undo operation registered clears the redo stack, this method posts an [`NSUndoManagerCheckpoint`](../nsnotification/name-swift.struct/nsundomanagercheckpoint.md) to allow clients to apply their pending operations before testing the redo stack.

## See Also

### Related Documentation
- [func redo()](./redo%28%29.md)
  Performs the operations in the last group on the redo stack, if there are any, recording them on the undo stack as a single group.
### Checking undo ability
- [var canUndo: Bool](./canundo.md)
  A Boolean value that indicates whether the manager has any actions to undo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/canredo)*