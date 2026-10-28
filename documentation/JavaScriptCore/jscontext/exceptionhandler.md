# exceptionHandler

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

A block to be invoked should evaluating a script result in a JavaScript exception being thrown.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var exceptionHandler: ((JSContext?, JSValue?) -> Void)! { get set }
```

```objc
@property (copy) void (^exceptionHandler)(JSContext *context, JSValue *exception);
```

## Discussion

The block takes the following parameters:

- **context**: The context in which the exception originates.
- **exception**: The JavaScript exception thrown.

The default value exception handler block stores its `exception` parameter value into the context’s [`exception`](./exception.md) property. As a consequence, the default behavior is that unhandled exceptions occurring within a callback from JavaScript to native code are thrown again upon return. Setting this value to `nil` results in all uncaught exceptions being silently consumed.

## See Also

### Working with JavaScript global state
- [var globalObject: JSValue!](./globalobject.md)
  The JavaScript global object associated with the context.
- [var exception: JSValue!](./exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var virtualMachine: JSVirtualMachine!](./virtualmachine.md)
  The JavaScript virtual machine to which the context belongs.
- [var name: String!](./name.md)
  A descriptive name for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/exceptionhandler)*