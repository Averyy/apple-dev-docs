# removeAllActions(withTarget:)

**Framework**: Foundation  
**Kind**: method

Clears the undo and redo stacks of all operations involving the specified target as the recipient of the undo message.

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
func removeAllActions(withTarget target: Any)
```

#### Discussion

Doesn’t re-enable the manager if it’s disabled.

## Parameters

- `target`: The recipient of the undo messages to be removed.

## See Also

- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [func removeAllActions()](undomanager/removeallactions.md)
  Clears the undo and redo stacks and reenables the manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/removeallactions(withtarget:))*