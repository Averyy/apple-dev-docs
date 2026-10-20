# BEKeyModifierFlags

**Framework**: BrowserEngineKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that records the state of the shift-modifier keys.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
enum BEKeyModifierFlags
```

```c
enum BEKeyModifierFlags : NSInteger;
```

## Topics

### Getting caps-shift information
- [BEKeyModifierFlags.capsLock](./bekeymodifierflags/capslock.md)
  A flag that indicates that the Caps Lock key is engaged.
- [BEKeyModifierFlags.shift](./bekeymodifierflags/shift.md)
  A flag that indicates that the Shift key is depressed.
- [BEKeyModifierFlags.none](./bekeymodifierflags/none.md)
  A flag that indicates no active key modifiers.
### Initializing the flags
- [init?(rawValue: Int)](./bekeymodifierflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Keyboard input
- [class BEKeyEntry](./bekeyentry.md)
  A class that represents a keyboard event in the text system.
- [class BEKeyEntryContext](./bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeymodifierflags)*