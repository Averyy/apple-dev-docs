# JSContext

**Framework**: JavaScriptCore  
**Kind**: class

A JavaScript execution environment.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class JSContext
```

#### Overview

You create and use JavaScript contexts to evaluate JavaScript scripts from Objective-C or Swift code; to access values that JavaScript defines or calculates; and to make native objects, methods, or functions accessible to JavaScript.

## Topics

### Creating JavaScript contexts
- [init!()](jscontext/init.md)
  Initializes a new JavaScript context.
- [init!(virtualMachine: JSVirtualMachine!)](jscontext/init(virtualmachine:).md)
  Creates a new JavaScript context associated with a specific virtual machine.
### Making JavaScript context inspectable
- [var isInspectable: Bool](jscontext/isinspectable.md)
  A Boolean value that indicates whether you can inspect the JavaScript context with Safari Web Inspector.
### Evaluating scripts
- [func evaluateScript(String!) -> JSValue!](jscontext/evaluatescript(_:).md)
  Executes the specified JavaScript code.
- [func evaluateScript(String!, withSourceURL: URL!) -> JSValue!](jscontext/evaluatescript(_:withsourceurl:).md)
  Executes the specified JavaScript code, treating the specified URL as its source location.
### Inspecting callback state in a running context
- [class func current() -> JSContext!](jscontext/current.md)
  Returns the context currently executing JavaScript code.
- [class func currentCallee() -> JSValue!](jscontext/currentcallee.md)
  Returns the currently executing JavaScript function.
- [class func currentThis() -> JSValue!](jscontext/currentthis.md)
  Returns the value of the `this` keyword in currently executing JavaScript code.
- [class func currentArguments() -> [Any]!](jscontext/currentarguments.md)
  Returns the arguments to the current native callback from JavaScript code.
### Working with JavaScript global state
- [var globalObject: JSValue!](jscontext/globalobject.md)
  The JavaScript global object associated with the context.
- [var exception: JSValue!](jscontext/exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var exceptionHandler: ((JSContext?, JSValue?) -> Void)!](jscontext/exceptionhandler.md)
  A block to be invoked should evaluating a script result in a JavaScript exception being thrown.
- [var virtualMachine: JSVirtualMachine!](jscontext/virtualmachine.md)
  The JavaScript virtual machine to which the context belongs.
- [var name: String!](jscontext/name.md)
  A descriptive name for the context.
### Accessing JavaScript global state with subscripts
- [func objectForKeyedSubscript(Any!) -> JSValue!](jscontext/objectforkeyedsubscript(_:).md)
  Returns the value of the specified JavaScript property in the context’s global object, allowing subscript getter syntax.
- [func setObject(Any!, forKeyedSubscript: (any NSCopying & NSObjectProtocol)!)](jscontext/setobject(_:forkeyedsubscript:).md)
  Sets the specified JavaScript property of the context’s global object, allowing subscript setter syntax.
### Working with the C JavaScriptCore API
- [var jsGlobalContextRef: JSGlobalContextRef!](jscontext/jsglobalcontextref.md)
  Returns the C representation of the JavaScript context.
- [init!(JSGlobalContextRef: JSGlobalContextRef!)](jscontext/init(jsglobalcontextref:).md)
  Creates a JavaScript context object from the equivalent C representation.

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

- [class JSVirtualMachine](jsvirtualmachine.md)
  A self-contained environment for JavaScript execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext)*