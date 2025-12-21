# makeLibXPCConnectionError()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Creates a new libXPC connection to the extension process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
func makeLibXPCConnectionError() throws -> xpc_connection_t
```

#### Return Value

The connection object representing the created libXPC connection or nil.

#### Discussion

This method creates a connection to the extension process and returns it. If it is not possible to make an XPC connection, this method will return nil and populate the `error` out param.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess/makelibxpcconnectionerror())*