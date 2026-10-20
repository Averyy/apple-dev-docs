# init(xpcRepresentation:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Creates a handle from a representation received in an XPC message.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(xpcRepresentation: xpc_object_t?) throws
```

```objc
+ (BELayerHierarchyHandle *) handleWithXPCRepresentation:(xpc_object_t) xpcRepresentation error:(NSError **) error;
```

## Parameters

- `xpcRepresentation`: A representation of the handle, encoded as an XPC object.

## See Also

### Sharing a layer hierarchy handle using XPC
- [func createXPCRepresentation() -> xpc_object_t](./createxpcrepresentation%28%29.md)
  Creates an object representing this handle that you send to another process in an XPC message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhandle/init(xpcrepresentation:))*