# disableUndoRegistration()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func disableUndoRegistration()
```

```objc
- (void) disableUndoRegistration;
```

#### Discussion

This method disables undos recorded by [`registerUndo(withTarget:selector:object:)`](./registerundo%28withtarget,selector,object%29.md) or invocation-based undo.

This method can be invoked multiple times by multiple clients. The [`enableUndoRegistration()`](./enableundoregistration%28%29.md) method must be invoked an equal number of times to re-enable undo registration.

## See Also

### Enabling and disabling undo
- [func enableUndoRegistration()](./enableundoregistration%28%29.md)
  Enables the recording of undo operations.
- [var isUndoRegistrationEnabled: Bool](./isundoregistrationenabled.md)
  A Boolean value that indicates whether the recording of undo operations is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/disableundoregistration())*