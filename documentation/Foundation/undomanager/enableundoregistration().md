# enableUndoRegistration()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func enableUndoRegistration()
```

```objc
- (void) enableUndoRegistration;
```

#### Discussion

Because undo registration is enabled by default, it is often used to balance a prior [`disableUndoRegistration()`](./disableundoregistration%28%29.md) message. Undo registration isn’t actually re-enabled until an enable message balances the last disable message in effect. Raises an `NSInternalInconsistencyException` if invoked while no [`disableUndoRegistration()`](./disableundoregistration%28%29.md) message is in effect.

## See Also

### Enabling and disabling undo
- [func disableUndoRegistration()](./disableundoregistration%28%29.md)
  Disables the recording of undo operations.
- [var isUndoRegistrationEnabled: Bool](./isundoregistrationenabled.md)
  A Boolean value that indicates whether the recording of undo operations is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/enableundoregistration())*