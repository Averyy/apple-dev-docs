# NSDeleteCommand

**Framework**: Foundation  
**Kind**: class

A command that deletes a scriptable object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSDeleteCommand
```

#### Overview

An instance of `NSDeleteCommand` deletes the specified scriptable object or objects (such as words, paragraphs, and so on).

Suppose, for example, a user executes a script that sends the command `delete the third rectangle in the first document` to the Sketch sample application (located in `/Developer/Examples/AppKit`). Cocoa creates an `NSDeleteCommand` object to perform the operation. When the command is executed, it uses the key-value coding mechanism (by invoking `removeValueAtIndex:fromPropertyWithKey:`) to remove the specified object or objects from their container. See the description for [`removeValue(at:fromPropertyWithKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/removeValue(at:fromPropertyWithKey:)) for related information.

`NSDeleteCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSDeleteCommand` or call its methods.

## Topics

### Working with specifiers
- [var keySpecifier: NSScriptObjectSpecifier](nsdeletecommand/keyspecifier.md)
  Returns a specifier for the object or objects to be deleted.
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](nsdeletecommand/setreceiversspecifier(_:).md)
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
- [class NSMoveCommand](nsmovecommand.md)
  A command that moves one or more scriptable objects.
- [class NSCreateCommand](nscreatecommand.md)
  A command that creates a scriptable object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeletecommand)*