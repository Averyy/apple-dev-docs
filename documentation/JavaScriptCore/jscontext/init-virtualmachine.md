# init(virtualMachine:)

**Framework**: JavaScriptCore  
**Kind**: init

Creates a new JavaScript context associated with a specific virtual machine.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(virtualMachine: JSVirtualMachine!)
```

#### Return Value

A new JavaScript context.

#### Discussion

By default, each context has an independent virtual machine (a [`JSVirtualMachine`](jsvirtualmachine.md) object). You cannot pass JavaScript values between contexts in different virtual machines. Use this initializer to create a context that shares its virtual machine with other JavaScript contexts to allow passing [`JSValue`](jsvalue.md) objects between those contexts.

## Parameters

- `virtualMachine`: The virtual machine with which to associate the new context.

## See Also

- [init!()](jscontext/init.md)
  Initializes a new JavaScript context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jscontext/init(virtualmachine:))*