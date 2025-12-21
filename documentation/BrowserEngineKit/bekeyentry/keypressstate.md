# BEKeyEntry.KeyPressState

**Framework**: BrowserEngineKit  
**Kind**: enum

An enumeration that represents the possible states of a key-press in a keyboard event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum KeyPressState
```

## Topics

### Key states
- [BEKeyEntry.KeyPressState.down](bekeyentry/keypressstate/down.md)
  The key is down.
- [BEKeyEntry.KeyPressState.up](bekeyentry/keypressstate/up.md)
  The key is up.
### Creating a key-press state
- [init?(rawValue: Int)](bekeyentry/keypressstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: BEKeyEntry.KeyPressState](bekeyentry/state.md)
  Type of the event, indicating whether it represents when the key is pressed or released.
- [var isKeyRepeating: Bool](bekeyentry/iskeyrepeating.md)
  Represents whether the event is repeating.
- [var timestamp: TimeInterval](bekeyentry/timestamp.md)
  Time at which the key event occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/keypressstate)*