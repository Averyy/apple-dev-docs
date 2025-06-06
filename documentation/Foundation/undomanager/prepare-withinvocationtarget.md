# prepare(withInvocationTarget:)

**Framework**: Foundation  
**Kind**: method

Prepares the undo manager for invocation-based undo with the given target as the subject of the next undo operation.

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
func prepare(withInvocationTarget target: Any) -> Any
```

#### Return Value

A proxy object that forwards messages to the undo manager for recording as undo actions.

## Parameters

- `target`: The undo manager maintains a weak reference to  .

## See Also

- [func registerUndo<TargetType>(withTarget: TargetType, handler: (TargetType) -> Void)](undomanager/registerundo(withtarget:handler:).md)
  Registers the specified closure to implement a single undo operation that the target receives.
- [func registerUndo(withTarget: Any, selector: Selector, object: Any?)](undomanager/registerundo(withtarget:selector:object:).md)
  Registers the selector of the specified target to implement a single undo operation that the target receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/prepare(withinvocationtarget:))*