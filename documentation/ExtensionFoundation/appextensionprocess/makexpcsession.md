# makeXPCSession()

**Framework**: ExtensionFoundation  
**Kind**: method

Connect to the app extension process using an XPC session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func makeXPCSession() throws -> XPCSession
```

#### Return Value

The session object your app uses to communicate with the app extension.

#### Discussion

Call this method to create a connection between your host app and an app extension using the XPC framework. You might choose this approach to connect a more secure connection to an app extension running in a sandboxed process. If the app extension accepts the connection request, the returned connection object contains the proxy information you need to communicate with it. If the app extension refuses the request or doesn’t support this connection type, this method throws an error.

## See Also

- [func makeXPCConnection() throws -> NSXPCConnection](appextensionprocess/makexpcconnection.md)
  Connect to the app extension process using the XPC types of the Foundation framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/makexpcsession())*