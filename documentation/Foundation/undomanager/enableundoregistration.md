# enableUndoRegistration()

**Framework**: Foundation  
**Kind**: method

Enables the recording of undo operations.

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
func enableUndoRegistration()
```

#### Discussion

Because undo registration is enabled by default, it is often used to balance a prior [`disableUndoRegistration()`](undomanager/disableundoregistration().md) message. Undo registration isn’t actually re-enabled until an enable message balances the last disable message in effect. Raises an `NSInternalInconsistencyException` if invoked while no [`disableUndoRegistration()`](undomanager/disableundoregistration().md) message is in effect.

## See Also

- [func disableUndoRegistration()](undomanager/disableundoregistration.md)
  Disables the recording of undo operations.
- [var isUndoRegistrationEnabled: Bool](undomanager/isundoregistrationenabled.md)
  A Boolean value that indicates whether the recording of undo operations is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/enableundoregistration())*