# makeLibXPCConnection()

**Framework**: BrowserEngineKit  
**Kind**: method

Creates a new XPC connection to the extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func makeLibXPCConnection() throws -> xpc_connection_t
```

#### Return Value

An object that represents the new XPC connection.

#### Discussion

When you create an [`xpc_connection_t`](https://developer.apple.com/documentation/xpc/xpc_connection_t) in your browser app using this method, the system calls your extension’s [`handle(xpcConnection:)`](networkingextension/handle(xpcconnection:).md) method to supply the remote end of the connection to your extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess/makelibxpcconnection())*