# isUndoRegistrationEnabled

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if registration is enabled; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

The default is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func disableUndoRegistration()](undomanager/disableundoregistration.md)
  Disables the recording of undo operations.
- [func enableUndoRegistration()](undomanager/enableundoregistration.md)
  Enables the recording of undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/isundoregistrationenabled)*