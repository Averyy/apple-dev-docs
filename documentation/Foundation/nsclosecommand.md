# NSCloseCommand

**Framework**: Foundation  
**Kind**: class

A command that closes one or more scriptable objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSCloseCommand
```

#### Overview

An instance of `NSCloseCommand` closes the specified scriptable object or objects—typically a document or window (and its associated document, if any). The command may optionally specify a location to save in and how to handle modified documents (by automatically saving changes, not saving them, or asking the user).

`NSCloseCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `close` command through key-value coding. Most applications don’t need to subclass `NSCloseCommand` or call its methods.

## Topics

### Accessing save options
- [var saveOptions: NSSaveOptions](nsclosecommand/saveoptions.md)
  Returns a constant indicating how to deal with closing any modified documents.
### Constants
- [enum NSSaveOptions](nssaveoptions.md)
  The [`saveOptions`](nsclosecommand/saveoptions.md) method returns one of the following constants to indicate how to deal with saving any modified documents:

## Relationships

### Inherits From
- [NSScriptCommand](nsscriptcommand.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSScriptCommand](nsscriptcommand.md)
  A self-contained scripting statement.
- [class NSQuitCommand](nsquitcommand.md)
  A command that quits the specified app.
- [class NSSetCommand](nssetcommand.md)
  A command that sets one or more attributes or relationships to one or more values.
- [class NSMoveCommand](nsmovecommand.md)
  A command that moves one or more scriptable objects.
- [class NSCreateCommand](nscreatecommand.md)
  A command that creates a scriptable object.
- [class NSDeleteCommand](nsdeletecommand.md)
  A command that deletes a scriptable object.
- [class NSExistsCommand](nsexistscommand.md)
  A command that determines whether a scriptable object exists.
- [class NSGetCommand](nsgetcommand.md)
  A command that retrieves a value or object from a scriptable object.
- [class NSCloneCommand](nsclonecommand.md)
  A command that clones one or more scriptable objects.
- [class NSCountCommand](nscountcommand.md)
  A command that counts the number of objects of a specified class in the specified object container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclosecommand)*