# globalObject

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

The JavaScript global object associated with the context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var globalObject: JSValue! { get }
```

```objc
@property (strong, readonly) JSValue * globalObject;
```

#### Discussion

In a web browser, the global object of a JavaScript context is the browser window (the `window` object in JavaScript). Outside of web-browser use, a context’s global object serves a similar role, separating the JavaScript namespaces of different contexts. Global variables within a script appear as fields or subscripts in the global object—you can access them either through this [`JSValue`](../jsvalue.md) object or through the methods listed in the Accessing JavaScript global state with subscripts section in [`JSContext`](../jscontext.md).

> **Note**:  For [`JSContext`](../jscontext.md) instances originating in WebKit, this method returns a reference to the `WindowProxy` object.

## See Also

### Working with JavaScript global state
- [var exception: JSValue!](./exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var exceptionHandler: ((JSContext?, JSValue?) -> Void)!](./exceptionhandler.md)
  A block to be invoked should evaluating a script result in a JavaScript exception being thrown.
- [var virtualMachine: JSVirtualMachine!](./virtualmachine.md)
  The JavaScript virtual machine to which the context belongs.
- [var name: String!](./name.md)
  A descriptive name for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/globalobject)*