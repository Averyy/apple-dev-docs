# init(xpcRepresentation:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a handle from a representation received in an XPC message.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(xpcRepresentation: xpc_object_t?) throws
```

## Parameters

- `xpcRepresentation`: A representation of the handle, encoded as an XPC object.

## See Also

- [init?(coder: NSCoder)](layerhierarchyhandle/init(coder:).md)
  Creates a handle from an encoded representation.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhandle/createxpcrepresentation.md)
  Creates an object representing this handle that you send to another process in an XPC message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/init(xpcrepresentation:))*