# BEKeyEntry.KeyPressState

**Framework**: BrowserEngineKit  
**Kind**: enum

Key-press states for a keyboard event.

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
  An entry that indicates the key is down.
- [BEKeyEntry.KeyPressState.up](bekeyentry/keypressstate/up.md)
  An entry that indicates the key is up.
### Creating a key-press state
- [init?(rawValue: Int)](bekeyentry/keypressstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var state: BEKeyEntry.KeyPressState](bekeyentry/state.md)
  A value that indicates if the key is pressed.
- [var isKeyRepeating: Bool](bekeyentry/iskeyrepeating.md)
  A Boolean value that indicates whether the person holds a key down to repeat its key event.
- [var timestamp: TimeInterval](bekeyentry/timestamp.md)
  The time that the key event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/keypressstate)*