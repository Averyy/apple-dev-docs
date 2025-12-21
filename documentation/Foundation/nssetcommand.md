# NSSetCommand

**Framework**: Foundation  
**Kind**: class

A command that sets one or more attributes or relationships to one or more values.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSSetCommand
```

#### Overview

An instance of `NSSetCommand` sets one or more attributes or relationships to one or more values; for example, it may set the (x, y) coordinates for a window’s position or set the name of a document.

`NSSetCommand` is part of Cocoa’s built-in scripting support. It works automatically to support the `set` command through key-value coding. Most applications don’t need to subclass `NSSetCommand` or call its methods.

`NSSetCommand` uses available scripting class descriptions to determine whether it should set a value for an attribute (or property), or set a value for all elements (to-many objects). For the latter, it invokes [`replaceValue(at:inPropertyWithKey:withValue:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/replaceValue(at:inPropertyWithKey:withValue:)); for the former, it invokes [`setValue(_:forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKey:)) (or, if the receiver overrides [`takeValue(_:forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/takeValue(_:forKey:)), it invokes that method, to support backward binary compatibility.)

For information on working with `set` commands, see [`Getting and Setting Properties and Elements`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_get_set/SAppsGetSet.html#//apple_ref/doc/uid/TP40002164-CH18) in [`Cocoa Scripting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Topics

### Working with specifiers
- [var keySpecifier: NSScriptObjectSpecifier](nssetcommand/keyspecifier.md)
  Returns a specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](nssetcommand/setreceiversspecifier(_:).md)
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
- [class NSCloseCommand](nsclosecommand.md)
  A command that closes one or more scriptable objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssetcommand)*