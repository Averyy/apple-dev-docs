# makeXPCConnection()

**Framework**: ExtensionFoundation  
**Kind**: method

Connect to the app extension process using the XPC types of the Foundation framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
func makeXPCConnection() throws -> NSXPCConnection
```

#### Return Value

The connection object your app uses to communicate with the app extension.

#### Discussion

Call this method to create a connection between your host app and an app extension using the types of the Foundation framework. If the app extension accepts the connection request, the returned connection object contains the proxy information you need to communicate with it. If the app extension refuses the request or doesn’t support this connection type, this method throws an error.

## See Also

- [func makeXPCSession() throws -> XPCSession](appextensionprocess/makexpcsession.md)
  Connect to the app extension process using an XPC session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/makexpcconnection())*