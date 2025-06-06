# createXPCRepresentation()

**Framework**: BrowserEngineKit  
**Kind**: method

Creates an object representing this handle that you send to another process in an XPC message.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func createXPCRepresentation() -> xpc_object_t
```

## See Also

- [init?(coder: NSCoder)](layerhierarchyhandle/init(coder:).md)
  Creates a handle from an encoded representation.
- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhandle/init(xpcrepresentation:).md)
  Creates a handle from a representation received in an XPC message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/createxpcrepresentation())*