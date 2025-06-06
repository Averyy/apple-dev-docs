# NSScriptExecutionContext

**Framework**: Foundation  
**Kind**: class

The context in which the current script command is executed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptExecutionContext
```

#### Overview

An `NSScriptExecutionContext` object is a shared instance (there is only one instance of the class) that represents the context in which the current script command is executed. `NSScriptExecutionContext` tracks global state relating to the command being executed, especially the top-level container object (that is, the container implied by a specifier object that specifies no container) used in an evaluation of an [`NSScriptObjectSpecifier`](nsscriptobjectspecifier.md) object.

In most cases, the top-level container for a complete series of nested object specifiers is automatically set to the application object (`NSApp`), and you can get this object with the [`topLevelObject`](nsscriptexecutioncontext/toplevelobject.md) method. But you can also set this top-level container to something else (using [`topLevelObject`](nsscriptexecutioncontext/toplevelobject.md)) if the situation warrants it.

It is unlikely that you will need to subclass `NSScriptExecutionContext`.

## Topics

### Getting the current context
- [class func shared() -> NSScriptExecutionContext](nsscriptexecutioncontext/shared.md)
  Returns the shared `NSScriptExecutionContext` instance.
### Getting and setting the container object
- [var topLevelObject: Any?](nsscriptexecutioncontext/toplevelobject.md)
  Sets the top-level object for an object-specifier evaluation.
- [var objectBeingTested: Any?](nsscriptexecutioncontext/objectbeingtested.md)
  Sets the top-level container object currently being tested in a “whose” qualifier to a given object.
- [var rangeContainerObject: Any?](nsscriptexecutioncontext/rangecontainerobject.md)
  Sets the top-level container object for a range-specifier evaluation to a give object.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext)*