# removeAllActions()

**Framework**: Foundation  
**Kind**: method

Clears the undo and redo stacks and reenables the manager.

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
func removeAllActions()
```

## See Also

- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [func removeAllActions(withTarget: Any)](undomanager/removeallactions(withtarget:).md)
  Clears the undo and redo stacks of all operations involving the specified target as the recipient of the undo message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/removeallactions())*