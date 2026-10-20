# name

**Framework**: JavaScriptCore  
**Kind**: property  
**Role**: Instance Property

A descriptive name for the context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String! { get set }
```

```objc
@property (copy) NSString * name;
```

#### Discussion

This name appears when using remote debugging to examine the context.

## See Also

### Working with JavaScript global state
- [var globalObject: JSValue!](./globalobject.md)
  The JavaScript global object associated with the context.
- [var exception: JSValue!](./exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var exceptionHandler: ((JSContext?, JSValue?) -> Void)!](./exceptionhandler.md)
  A block to be invoked should evaluating a script result in a JavaScript exception being thrown.
- [var virtualMachine: JSVirtualMachine!](./virtualmachine.md)
  The JavaScript virtual machine to which the context belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/name)*