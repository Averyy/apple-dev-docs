# canUndo

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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
var canUndo: Bool { get }
```

```objc
@property (readonly) BOOL canUndo;
```

## Discussion

[`true`](../../Swift/true.md) if the manager has any actions to undo, otherwise [`false`](../../Swift/false.md).

The return value doesn’t mean you can safely invoke [`undo()`](./undo%28%29.md) or [`undoNestedGroup()`](./undonestedgroup%28%29.md)—you may have to close open undo groups first.

## See Also

### Related Documentation
- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](./registerundo%28withtarget,selector,object%29.md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.
- [func enableUndoRegistration()](./enableundoregistration%28%29.md)
  Enables the recording of undo operations.
### Checking undo ability
- [var canRedo: Bool](./canredo.md)
  A Boolean value that indicates whether the manager has any actions to redo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/canundo)*