# name

**Framework**: JavaScriptCore  
**Kind**: property

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

#### Discussion

This name appears when using remote debugging to examine the context.

## See Also

- [var globalObject: JSValue!](jscontext/globalobject.md)
  The JavaScript global object associated with the context.
- [var exception: JSValue!](jscontext/exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var exceptionHandler: ((JSContext?, JSValue?) -> Void)!](jscontext/exceptionhandler.md)
  A block to be invoked should evaluating a script result in a JavaScript exception being thrown.
- [var virtualMachine: JSVirtualMachine!](jscontext/virtualmachine.md)
  The JavaScript virtual machine to which the context belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/name)*