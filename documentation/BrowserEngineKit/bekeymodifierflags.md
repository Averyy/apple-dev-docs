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
  A flag that indicates that the Caps Lock key is engaged.
- [BEKeyModifierFlags.shift](bekeymodifierflags/shift.md)
  A flag that indicates that the Shift key is depressed.
- [BEKeyModifierFlags.none](bekeymodifierflags/none.md)
  A flag that indicates no active key modifiers.
### Initializing the flags
- [init?(rawValue: Int)](bekeymodifierflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class BEKeyEntry](bekeyentry.md)
  A class that represents a keyboard event in the text system.
- [class BEKeyEntryContext](bekeyentrycontext.md)
  A class that describes a key event and the text document with which the event is associated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeymodifierflags)*