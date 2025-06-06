# init()

**Framework**: JavaScriptCore  
**Kind**: init

Initializes a new JavaScript context.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!()
```

#### Return Value

A new JavaScript context.

#### Discussion

This initializer creates a context along with a new, independent virtual machine (a [`JSVirtualMachine`](jsvirtualmachine.md) object). You cannot pass JavaScript values ([`JSValue`](jsvalue.md) objects) between contexts in different virtual machines. To create contexts that share a virtual machine, use the [`init(virtualMachine:)`](jscontext/init(virtualmachine:).md) initializer.

## See Also

- [init!(virtualMachine: JSVirtualMachine!)](jscontext/init(virtualmachine:).md)
  Creates a new JavaScript context associated with a specific virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/init())*