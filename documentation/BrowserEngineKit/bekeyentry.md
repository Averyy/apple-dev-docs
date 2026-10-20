# BEKeyEntry

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface BEKeyEntry : NSObject
```

## Topics

### Identifying the key
- [var key: UIKey](./bekeyentry/key.md)
  The key that the person presses.
### Getting information about the keypress
- [var state: BEKeyEntry.KeyPressState](./bekeyentry/state.md)
  A value that indicates if the key is pressed.
- [BEKeyEntry.KeyPressState](./bekeyentry/keypressstate.md)
  Key-press states for a keyboard event.
- [var isKeyRepeating: Bool](./bekeyentry/iskeyrepeating.md)
  A Boolean value that indicates whether the person holds a key down to repeat its key event.
- [var timestamp: TimeInterval](./bekeyentry/timestamp.md)
  The time that the key event occurs.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Keyboard input
- [class BEKeyEntryContext](./bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.
- [enum BEKeyModifierFlags](./bekeymodifierflags.md)
  An enumeration that records the state of the shift-modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry)*