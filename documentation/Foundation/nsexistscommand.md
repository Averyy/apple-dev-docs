# NSExistsCommand

**Framework**: Foundation  
**Kind**: class

A command that determines whether a scriptable object exists.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSExistsCommand
```

#### Overview

An instance of `NSExistsCommand` determines whether a specified scriptable object, such as a word, paragraph, or image, exists.

When an instance of `NSExistsCommand` is executed, it evaluates the receiver specifier for the command to determine if it specifies any objects.

`NSExistsCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSExistsCommand`.

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

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
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
- [class NSGetCommand](nsgetcommand.md)
  A command that retrieves a value or object from a scriptable object.
- [class NSCloneCommand](nsclonecommand.md)
  A command that clones one or more scriptable objects.
- [class NSCountCommand](nscountcommand.md)
  A command that counts the number of objects of a specified class in the specified object container.
- [class NSCloseCommand](nsclosecommand.md)
  A command that closes one or more scriptable objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexistscommand)*