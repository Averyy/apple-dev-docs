# NSScriptCoercionHandler

**Framework**: Foundation  
**Kind**: class

A mechanism for converting one kind of scripting data to another.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptCoercionHandler
```

#### Overview

A shared instance of this class coerces (converts) object values to objects of another class using information supplied by classes that register with it. Coercions frequently are required during key-value coding.

## Topics

### Accessing the application’s handler
- [class func shared() -> NSScriptCoercionHandler](nsscriptcoercionhandler/shared.md)
  Returns the shared `NSScriptCoercionHandler` for the application.
### Working with handlers
- [func coerceValue(Any, to: AnyClass) -> Any?](nsscriptcoercionhandler/coercevalue(_:to:).md)
  Returns an object of a given class representing a given value.
- [func registerCoercer(Any, selector: Selector, toConvertFrom: AnyClass, to: AnyClass)](nsscriptcoercionhandler/registercoercer(_:selector:toconvertfrom:to:).md)
  Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.

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
- [class NSScriptExecutionContext](nsscriptexecutioncontext.md)
  The context in which the current script command is executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler)*