# BEKeyEntry.KeyPressState

**Framework**: BrowserEngineKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum BEKeyPressState : NSInteger;
```

## Topics

### Key states
- [BEKeyEntry.KeyPressState.down](./keypressstate/down.md)
  An entry that indicates the key is down.
- [BEKeyEntry.KeyPressState.up](./keypressstate/up.md)
  An entry that indicates the key is up.
### Creating a key-press state
- [init?(rawValue: Int)](./keypressstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting information about the keypress
- [var state: BEKeyEntry.KeyPressState](./state.md)
  A value that indicates if the key is pressed.
- [var isKeyRepeating: Bool](./iskeyrepeating.md)
  A Boolean value that indicates whether the person holds a key down to repeat its key event.
- [var timestamp: TimeInterval](./timestamp.md)
  The time that the key event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/keypressstate)*