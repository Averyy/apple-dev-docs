# disableUndoRegistration()

**Framework**: Foundation  
**Kind**: method

Disables the recording of undo operations.

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
func disableUndoRegistration()
```

#### Discussion

This method disables undos recorded by [`registerUndo(withTarget:selector:object:)`](undomanager/registerundo(withtarget:selector:object:).md) or invocation-based undo.

This method can be invoked multiple times by multiple clients. The [`enableUndoRegistration()`](undomanager/enableundoregistration().md) method must be invoked an equal number of times to re-enable undo registration.

## See Also

- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.
- [var isUndoRegistrationEnabled: Bool](undomanager/isundoregistrationenabled.md)
  A Boolean value that indicates whether the recording of undo operations is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/disableundoregistration())*