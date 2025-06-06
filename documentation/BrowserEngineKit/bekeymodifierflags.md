# BEKeyModifierFlags

**Framework**: BrowserEngineKit  
**Kind**: enum

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

## Topics

### Getting caps-shift information
- [BEKeyModifierFlags.capsLock](bekeymodifierflags/capslock.md)
  The caps lock is engaged.
- [BEKeyModifierFlags.shift](bekeymodifierflags/shift.md)
  The shift key is pressed down.
- [BEKeyModifierFlags.none](bekeymodifierflags/none.md)
  There aren’t any active key modifiers.
### Initializing the flags
- [init?(rawValue: Int)](bekeymodifierflags/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](bekeymodifierflags/equatable-implementations.md)
- [RawRepresentable Implementations](bekeymodifierflags/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class BEKeyEntry](bekeyentry.md)
  A class that represents a keyboard event in the text system.
- [class BEKeyEntryContext](bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeymodifierflags)*