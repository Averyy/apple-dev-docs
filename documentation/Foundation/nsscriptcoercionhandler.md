# NSScriptCoercionHandler

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A mechanism for converting one kind of scripting data to another.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSScriptCoercionHandler
```

```objc
@interface NSScriptCoercionHandler : NSObject
```

## Overview

A shared instance of this class coerces (converts) object values to objects of another class using information supplied by classes that register with it. Coercions frequently are required during key-value coding.

## Topics

### Accessing the application’s handler
- [class func shared() -> NSScriptCoercionHandler](./nsscriptcoercionhandler/shared%28%29.md)
  Returns the shared `NSScriptCoercionHandler` for the application.
### Working with handlers
- [func coerceValue(Any, to: AnyClass) -> Any?](./nsscriptcoercionhandler/coercevalue%28_,to%29.md)
  Returns an object of a given class representing a given value.
- [func registerCoercer(Any, selector: Selector, toConvertFrom: AnyClass, to: AnyClass)](./nsscriptcoercionhandler/registercoercer%28_,selector,toconvertfrom,to%29.md)
  Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### NSObject Script Support
- [NSComparisonMethods](./nscomparisonmethods.md)
  A collection of default comparison methods useful for performing specifier tests.
- [NSScriptingComparisonMethods](../ObjectiveC/nsscriptingcomparisonmethods.md)
  A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../ObjectiveC/nsscriptkeyvaluecoding.md)
  A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](./nsscriptobjectspecifiers.md)
  A collection of methods providing additional object specifier functionality.
- [class NSScriptExecutionContext](./nsscriptexecutioncontext.md)
  The context in which the current script command is executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler)*