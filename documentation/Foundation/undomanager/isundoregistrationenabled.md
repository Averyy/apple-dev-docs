# isUndoRegistrationEnabled

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the recording of undo operations is enabled.

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
var isUndoRegistrationEnabled: Bool { get }
```

```objc
@property (readonly, getter=isUndoRegistrationEnabled) BOOL undoRegistrationEnabled;
```

#### Discussion

[`true`](../../Swift/true.md) if registration is enabled; otherwise, [`false`](../../Swift/false.md).

The default is [`true`](../../Swift/true.md).

## See Also

### Enabling and disabling undo
- [func disableUndoRegistration()](./disableundoregistration%28%29.md)
  Disables the recording of undo operations.
- [func enableUndoRegistration()](./enableundoregistration%28%29.md)
  Enables the recording of undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/isundoregistrationenabled)*