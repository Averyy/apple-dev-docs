# init(coder:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a handle from an encoded representation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder`: An object that contains data that describes the handle to create.

## See Also

- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhandle/init(xpcrepresentation:).md)
  Creates a handle from a representation received in an XPC message.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhandle/createxpcrepresentation.md)
  Creates an object representing this handle that you send to another process in an XPC message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/init(coder:))*