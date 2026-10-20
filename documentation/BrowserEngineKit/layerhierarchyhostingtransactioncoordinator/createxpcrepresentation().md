# createXPCRepresentation()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a representation of the transaction coordinator that you send to another process.

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

### Sharing a transaction coordinator using XPC
- [init(xpcRepresentation: xpc_object_t?) throws](./init%28xpcrepresentation%29.md)
  Creates a transaction coordinator from an XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/createxpcrepresentation())*