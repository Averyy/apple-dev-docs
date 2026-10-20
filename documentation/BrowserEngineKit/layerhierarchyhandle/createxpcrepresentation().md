# createXPCRepresentation()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates an object representing this handle that you send to another process in an XPC message.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func createXPCRepresentation() -> xpc_object_t
```

```objc
- (xpc_object_t) createXPCRepresentation;
```

## See Also

### Sharing a layer hierarchy handle using XPC
- [init(xpcRepresentation: xpc_object_t?) throws](./init%28xpcrepresentation%29.md)
  Creates a handle from a representation received in an XPC message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/createxpcrepresentation())*