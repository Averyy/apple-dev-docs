# NSMoveCommand

**Framework**: Foundation  
**Kind**: class

A command that moves one or more scriptable objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSMoveCommand
```

#### Overview

An instance of `NSMoveCommand` moves the specified scriptable object or objects; for example, it may move words to a new location in a document or a file to a new directory.

`NSMoveCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `move` AppleScript command through key-value coding. Most applications don’t need to subclass `NSMoveCommand` or invoke its methods. However, for circumstances where you might choose to subclass this command, see “Modifying a Standard Command” in [`Script Commands`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

When an instance of `NSMoveCommand` is executed, it does not make copies of moved objects. It removes objects from the source container or containers, then inserts them into the destination container.

## Topics

### Working with specifiers
- [var keySpecifier: NSScriptObjectSpecifier](nsmovecommand/keyspecifier.md)
  Returns a specifier for the object or objects to be moved.
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](nsmovecommand/setreceiversspecifier(_:).md)
  Sets the receiver’s object specifier.

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
- [class NSCloseCommand](nsclosecommand.md)
  A command that closes one or more scriptable objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmovecommand)*