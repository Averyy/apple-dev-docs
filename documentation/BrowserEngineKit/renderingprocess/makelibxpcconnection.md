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

#### Overview

When you create an [`xpc_connection_t`](https://developer.apple.com/documentation/XPC/xpc_connection_t) in your browser app using this method, the operating system calls your extension’s [`handle(xpcConnection:)`](renderingextension/handle(xpcconnection:).md) method to supply the remote end of the connection to your extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/renderingprocess/makelibxpcconnection())*