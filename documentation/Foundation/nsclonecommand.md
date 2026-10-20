# NSCloneCommand

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A command that clones one or more scriptable objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSCloneCommand
```

```objc
@interface NSCloneCommand : NSScriptCommand
```

#### Overview

An instance of `NSCloneCommand` clones the specified scriptable object or objects (such as words, paragraphs, images, and so on) and inserts them in the specified location, or the default location if no location is specified. The cloned scriptable objects typically correspond to objects in the application, but aren’t required to. This command corresponds to AppleScript’s `duplicate` command.

`NSCloneCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `duplicate` command through key-value coding. Most applications don’t need to subclass `NSCloneCommand` or invoke its methods.

When an instance of `NSCloneCommand` is executed, it clones the specified objects by sending them [`copyWithZone:`](../ObjectiveC/nsobject-swift.class/copywithzone_.md) messages.

## Topics

### Working with specifiers
- [var keySpecifier: NSScriptObjectSpecifier](./nsclonecommand/keyspecifier.md)
  Returns a specifier for the object or objects to be cloned.
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](./nsclonecommand/setreceiversspecifier%28_%29.md)
  Sets the receiver’s object specifier;.

## Relationships

### Inherits From
- [NSScriptCommand](./nsscriptcommand.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Script Commands
- [class NSScriptCommand](./nsscriptcommand.md)
  A self-contained scripting statement.
- [class NSQuitCommand](./nsquitcommand.md)
  A command that quits the specified app.
- [class NSSetCommand](./nssetcommand.md)
  A command that sets one or more attributes or relationships to one or more values.
- [class NSMoveCommand](./nsmovecommand.md)
  A command that moves one or more scriptable objects.
- [class NSCreateCommand](./nscreatecommand.md)
  A command that creates a scriptable object.
- [class NSDeleteCommand](./nsdeletecommand.md)
  A command that deletes a scriptable object.
- [class NSExistsCommand](./nsexistscommand.md)
  A command that determines whether a scriptable object exists.
- [class NSGetCommand](./nsgetcommand.md)
  A command that retrieves a value or object from a scriptable object.
- [class NSCountCommand](./nscountcommand.md)
  A command that counts the number of objects of a specified class in the specified object container.
- [class NSCloseCommand](./nsclosecommand.md)
  A command that closes one or more scriptable objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclonecommand)*