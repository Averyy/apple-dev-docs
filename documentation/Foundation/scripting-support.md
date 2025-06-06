# Scripting Support

**Framework**: Foundation

Allow users to control your app with AppleScript and other automation technologies, or run scripts from within your app.

## Topics

### Script Execution
- [class NSAppleScript](nsapplescript.md)
  An object that provides the ability to load, compile, and execute scripts.
### Apple Event Handling
- [class NSAppleEventDescriptor](nsappleeventdescriptor.md)
  A wrapper for the Apple event descriptor data type.
- [class NSAppleEventManager](nsappleeventmanager.md)
  A mechanism for registering handler routines for specific types of Apple events and dispatching events to those handlers.
### Script Commands
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
- [class NSCloseCommand](nsclosecommand.md)
  A command that closes one or more scriptable objects.
### Object Specifiers
- [class NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
  An abstract class used to represent natural language expressions.
- [class NSPropertySpecifier](nspropertyspecifier.md)
  A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [class NSPositionalSpecifier](nspositionalspecifier.md)
  A specifier for an insertion point in a container relative to another object in the container.
- [class NSRandomSpecifier](nsrandomspecifier.md)
  A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSRangeSpecifier](nsrangespecifier.md)
  A specifier for a range of objects in a container.
- [class NSUniqueIDSpecifier](nsuniqueidspecifier.md)
  A specifier for an object in a collection (or container) by unique ID.
- [class NSWhoseSpecifier](nswhosespecifier.md)
  A specifier that indicates every object in a collection matching a condition.
- [class NSNameSpecifier](nsnamespecifier.md)
  A specifier for an object in a collection (or container) by name.
- [class NSMiddleSpecifier](nsmiddlespecifier.md)
  A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSIndexSpecifier](nsindexspecifier.md)
  A specifier representing an object in a collection (or container) with an index number.
- [class NSRelativeSpecifier](nsrelativespecifier.md)
  A specifier that indicates an object in a collection by its position relative to another object.
### Script Dictionary Description
- [class NSScriptSuiteRegistry](nsscriptsuiteregistry.md)
  The top-level repository of scriptability information for an app at runtime.
- [class NSScriptClassDescription](nsscriptclassdescription.md)
  A scriptable class that a macOS app supports.
- [class NSClassDescription](nsclassdescription.md)
  An abstract class that provides the interface for querying the relationships and properties of a class.
- [class NSScriptCommandDescription](nsscriptcommanddescription.md)
  A script command that a macOS app supports.
### Object Matching Tests
- [class NSScriptWhoseTest](nsscriptwhosetest.md)
  An abstract class that provides the basis for testing specifiers one at a time or in groups.
- [class NSSpecifierTest](nsspecifiertest.md)
  A comparison between an object specifier and a test object.
- [class NSLogicalTest](nslogicaltest.md)
  The logical combination of one or more specifier tests.
### NSObject Script Support
- [NSComparisonMethods](nscomparisonmethods.md)
  A collection of default comparison methods useful for performing specifier tests.
- [NSScriptingComparisonMethods](../ObjectiveC/nsscriptingcomparisonmethods.md)
  A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../ObjectiveC/nsscriptkeyvaluecoding.md)
  A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md)
  A collection of methods providing additional object specifier functionality.
- [class NSScriptCoercionHandler](nsscriptcoercionhandler.md)
  A mechanism for converting one kind of scripting data to another.
- [class NSScriptExecutionContext](nsscriptexecutioncontext.md)
  The context in which the current script command is executed.

## See Also

- [Task Management](task-management.md)
  Manage your app’s work and how it interacts with system services like Handoff and Shortcuts.
- [Resources](resources.md)
  Access assets and other data bundled with your app.
- [Notifications](notifications.md)
  Design patterns for broadcasting information and for subscribing to broadcasts.
- [App Extension Support](app-extension-support.md)
  Manage the interaction between an app extension and its hosting app.
- [Errors and Exceptions](errors-and-exceptions.md)
  Respond to problem situations in your interactions with APIs, and fine-tune your app for better debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scripting-support)*