# AppExtensionConfiguration

**Framework**: ExtensionFoundation  
**Kind**: protocol

An interface you use to configure the XPC connection in your app extension.

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
@MainActor
@preconcurrency protocol AppExtensionConfiguration : Sendable
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

Adopt this protocol in a custom type, and use that type to finalize the XPC connection to the host app. The host app tries to create an XPC connection to your app extension shortly after launching it. The system directs that connection request to the code in your configuration object. Use your code to provide the host with the information it needs to communicate with your app extension.

This protocol supports app extensions that don’t offer any custom UI. If your app extension provides custom UI, instead use the  [`AppExtensionSceneConfiguration`](https://developer.apple.com/documentation/ExtensionKit/AppExtensionSceneConfiguration) type from [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit).

## Topics

### Accepting a connection to the host app
- [func accept(connection: NSXPCConnection) -> Bool](appextensionconfiguration/accept(connection:).md)
  Returns a Boolean value that indicates whether you accept an incoming connection request from the host app.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [ConnectionHandler](connectionhandler.md)

## See Also

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)
  Create an app extension to perform tasks in a separate process from a host app.
- [protocol AppExtension](appextension.md)
  An interface you use to declare the content, structure, and behavior of an app extension.
- [struct ConnectionHandler](connectionhandler.md)
  A type that contains a custom closure that handles incoming XPC connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration)*