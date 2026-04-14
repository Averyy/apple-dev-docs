# BEKeyEntry

**Framework**: BrowserEngineKit  
**Kind**: class

A class that represents a keyboard event in the text system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BEKeyEntry
```

## Topics

### Identifying the key
- [var key: UIKey](bekeyentry/key.md)
  The key that the person presses.
### Getting information about the keypress
- [var state: BEKeyEntry.KeyPressState](bekeyentry/state.md)
  A value that indicates if the key is pressed.
- [BEKeyEntry.KeyPressState](bekeyentry/keypressstate.md)
  Key-press states for a keyboard event.
- [var isKeyRepeating: Bool](bekeyentry/iskeyrepeating.md)
  A Boolean value that indicates whether the person holds a key down to repeat its key event.
- [var timestamp: TimeInterval](bekeyentry/timestamp.md)
  The time that the key event occurs.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BEKeyEntryContext](bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.
- [enum BEKeyModifierFlags](bekeymodifierflags.md)
  An enumeration that records the state of the shift-modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry)*