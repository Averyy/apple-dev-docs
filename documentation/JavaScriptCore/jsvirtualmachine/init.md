# init()

**Framework**: JavaScriptCore  
**Kind**: init

Initializes a JavaScript virtual machine.

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

A new, independent JavaScript virtual machine.

#### Discussion

Use this initializer to create a virtual machine for use with more than one JavaScript context. By default, creating a [`JSContext`](jscontext.md) object automatically creates an independent virtual machine—to share a virtual machine between contexts, obtain a [`JSVirtualMachine`](jsvirtualmachine.md) instance and then create contexts using the [`init(virtualMachine:)`](jscontext/init(virtualmachine:).md) initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine/init())*