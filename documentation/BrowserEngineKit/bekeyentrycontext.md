# BEKeyEntryContext

**Framework**: BrowserEngineKit  
**Kind**: class

A class that describes a key event and the text document with which the event is associated.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
class BEKeyEntryContext
```

#### Overview

If the key entry occurs within the context of a composed input mode, for example Chinese, Japanese, or Korean input, set [`shouldEvaluateForInputSystemHandling`](bekeyentrycontext/shouldevaluateforinputsystemhandling.md) to `true`. The text system uses the document’s marked text to combine multiple key events into a single input character.

## Topics

### Creating a key entry context
- [init(keyEntry: BEKeyEntry)](bekeyentrycontext/init(keyentry:).md)
  Initializes an instance of BEKeyEventContext with its corresponding `keyState`
### Getting the information about the key event
- [var keyEntry: BEKeyEntry](bekeyentrycontext/keyentry.md)
  BEKeyEntry for which this context is representing.
- [var shouldInsertCharacter: Bool](bekeyentrycontext/shouldinsertcharacter.md)
  Represents whether a character should be inserted.
- [var shouldEvaluateForInputSystemHandling: Bool](bekeyentrycontext/shouldevaluateforinputsystemhandling.md)
  Represents whether the key event should be evaluated within the context of a composed input mode.
### Getting information about the text document
- [var isDocumentEditable: Bool](bekeyentrycontext/isdocumenteditable.md)
  Represents whether the web document is editable

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

- [class BEKeyEntry](bekeyentry.md)
  A class that represents a keyboard event in the text system.
- [enum BEKeyModifierFlags](bekeymodifierflags.md)
  An enumeration that records the state of the shift-modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentrycontext)*