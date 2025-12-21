# ConnectionHandler

**Framework**: ExtensionFoundation  
**Kind**: struct

A type that contains a custom closure that handles incoming XPC connections.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 1.1+

## Declaration

```swift
@MainActor
@preconcurrency struct ConnectionHandler
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

This type manages a closure in your app extension that accepts incoming XPC connections from a host app. Create an instance of this structure and initialize it with a closure for the type of XPC connection the host app uses with app extensions. Assign the instance you created to the [`configuration`](appextension/configuration-swift.property.md) property of your custom [`AppExtension`](appextension.md) type. When the host app tries to open a connection, the system runs your closure to accept that connection.

Use this type to establish connections with either the [`Foundation`](https://developer.apple.com/documentation/Foundation) or [`XPC`](https://developer.apple.com/documentation/XPC) framework.

## Topics

### Initializing the connection handler
- [init(onConnection: (NSXPCConnection) -> Bool)](connectionhandler/init(onconnection:).md)
  Initializes the connection handler with a closure that accepts a Foundation XPC object.
- [init(onSessionRequest: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)](connectionhandler/init(onsessionrequest:).md)
  Initializes the connection handler with a closure that accepts an XPC session.

## Relationships

### Conforms To
- [AppExtensionConfiguration](appextensionconfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)
  Create an app extension to perform tasks in a separate process from a host app.
- [protocol AppExtension](appextension.md)
  An interface you use to declare the content, structure, and behavior of an app extension.
- [protocol AppExtensionConfiguration](appextensionconfiguration.md)
  An interface you use to configure the XPC connection in your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/connectionhandler)*