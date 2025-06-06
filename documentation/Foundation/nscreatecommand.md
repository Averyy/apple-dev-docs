# NSCreateCommand

**Framework**: Foundation  
**Kind**: class

A command that creates a scriptable object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSCreateCommand
```

#### Overview

An instance of `NSCreateCommand` creates the specified scriptable object (such as a document), optionally supplying the new object with the specified attributes. This command corresponds to AppleScript’s `make` command.

`NSCreateCommand` is part of Cocoa’s built-in scripting support. Most applications don’t need to subclass `NSCreateCommand` or invoke its methods.

When an instance of `NSCreateCommand` is executed, it creates a new object using `[[theClassToBeCreated allocWithZone:NULL] init]` (where `theClassToBeCreated` is the class of the object to be created), unless the command has a `with data` argument. In the latter case, the new object is created by invoking `[[NSScriptCoercionHandler sharedCoercionHandler] coerceValue:theDataAsAnObject toClass:theClassToBeCreated]`.  Any properties specified by a `with properties` argument are then set in the new object using `-setScriptingProperties:`.

If an `NSCreateCommand` object with no argument corresponding to the `at` parameter is executed (for example, `tell application "Mail" to make new mailbox with properties {name:"testFolder"}`), and the receiver of the command (not necessarily the application object) has a to-many relationship to objects of the class to be instantiated, and the class description for the receiving class returns [`false`](https://developer.apple.com/documentation/swift/false) when sent an `isLocationRequiredToCreateForKey:` message, the `NSCreateCommand` object creates a new object and sends the receiver an [`insertValue(_:at:inPropertyWithKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/insertValue(_:at:inPropertyWithKey:)) message to place the new object in the container. This is part of Cocoa’s scripting support for inserting newly-created objects into containers without explicitly specifying a location.

## Topics

### Getting information about a create command
- [var createClassDescription: NSScriptClassDescription](nscreatecommand/createclassdescription.md)
  Returns the class description for the class that is to be created.
- [var resolvedKeyDictionary: [String : Any]](nscreatecommand/resolvedkeydictionary.md)
  Returns a dictionary that contains the properties that were specified in the `make` Apple event command that has been converted to this `NSCreateCommand` object.

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

- [class NSScriptCommand](nsscriptcommand.md)
  A self-contained scripting statement.
- [class NSQuitCommand](nsquitcommand.md)
  A command that quits the specified app.
- [class NSSetCommand](nssetcommand.md)
  A command that sets one or more attributes or relationships to one or more values.
- [class NSMoveCommand](nsmovecommand.md)
  A command that moves one or more scriptable objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscreatecommand)*