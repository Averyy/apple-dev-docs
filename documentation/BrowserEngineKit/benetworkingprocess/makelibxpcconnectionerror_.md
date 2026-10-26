# makeLibXPCConnectionError:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Creates a new XPC connection to the extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (xpc_connection_t) makeLibXPCConnectionError:(NSError **) error;
```

#### Return Value

An object that represents the new XPC connection, or `nil` if an error occurs.

#### Discussion

When you create an [`xpc_connection_t`](../../XPC/xpc_connection_t.md) in your browser app using this method, the system calls your extension’s [`handle(xpcConnection:)`](../networkingextension/handle%28xpcconnection%29.md) method to supply the remote end of the connection to your extension process.

## Parameters

- `error`: If an error occurs, upon return contains an [`NSError`](../../Foundation/nserror.md) object that describes the problem. If you don’t want information about errors that happen, pass in `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/benetworkingprocess/makelibxpcconnectionerror:)*