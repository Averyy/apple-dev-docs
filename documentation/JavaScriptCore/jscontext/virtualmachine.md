# virtualMachine

**Framework**: JavaScriptCore  
**Kind**: property

The JavaScript virtual machine to which the context belongs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var virtualMachine: JSVirtualMachine! { get }
```

#### Discussion

To create a context associated with a specific virtual machine, allowing JavaScript values to be passed between contexts that share the same virtual machine, use the [`init(virtualMachine:)`](jscontext/init(virtualmachine:).md) initializer.

## See Also

- [var globalObject: JSValue!](jscontext/globalobject.md)
  The JavaScript global object associated with the context.
- [var exception: JSValue!](jscontext/exception.md)
  A JavaScript exception to be thrown in evaluation of the script.
- [var exceptionHandler: ((JSContext?, JSValue?) -> Void)!](jscontext/exceptionhandler.md)
  A block to be invoked should evaluating a script result in a JavaScript exception being thrown.
- [var name: String!](jscontext/name.md)
  A descriptive name for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/virtualmachine)*