# accept(connection:)

**Framework**: ExtensionFoundation  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether you accept an incoming connection request from the host app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func accept(connection: NSXPCConnection) -> Bool
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Return Value

`true` if you accept the connection to the host app, or `false` if you don’t.

#### Discussion

Implement this method in your custom type and use it to establish communication between your app extension and the host app that made the request. To accept a connection request, set the connection’s [`exportedObject`](https://developer.apple.com/documentation/Foundation/NSXPCConnection/exportedObject) property to an object in your app extension that implements a protocol or type from the host’s SDK. Similarly, put the type information in the [`exportedInterface`](https://developer.apple.com/documentation/Foundation/NSXPCConnection/exportedInterface) property. You can also retrieve other relevant properties of the connection object, such as the remote connection details, and use them to set up your app extension. When you’re ready to start communicating with the host, call the connection’s [`resume()`](https://developer.apple.com/documentation/Foundation/NSXPCConnection/resume()) method and then return `true` from this method.

## Parameters

- `connection`: A connection object you can use to communicate with the host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration/accept(connection:))*