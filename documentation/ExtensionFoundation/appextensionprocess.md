# AppExtensionProcess

**Framework**: ExtensionFoundation  
**Kind**: struct

A type the host app creates to launch and manage an app extension.

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
struct AppExtensionProcess
```

## Mentions

- [Adding support for app extensions to your app](adding-support-for-app-extensions-to-your-app.md)

#### Overview

Create this type from your host app when you want to communicate with an available app extension. This type creates a new process, and runs the app extension’s startup code in that process. After startup, establish an XPC connection to the app extension’s process using the methods of this type. Use that XPC connection to communicate with the app extension.

When creating an instance of this type, you specify which app extension to launch using an [`AppExtensionIdentity`](appextensionidentity.md) type. If the app extension is already running, creating the `AppExtensionProcess` type configures it with the already running process. If the app extension isn’t yet running, creating this type forks a new process and runs the app extension’s startup code in it. In both cases, you receive an instance of this structure only after the app extension is running and ready for you to establish an XPC connection.

Maintain a reference to this structure for as long as you need to communicate with the app extension. When you no longer need the app extension, call the `invalidate` method to release your app’s reference to the process. If the app extension process exits for any reason, the system calls the [`onInterruption`](appextensionprocess/configuration/oninterruption.md) handler you provided at configuration time.

## Topics

### Creating the app-extension process
- [init(configuration: AppExtensionProcess.Configuration) throws](appextensionprocess/init(configuration:)-2g0cy.md)
  Finds an existing process for the specified app extension or creates a new one synchronously.
- [init(configuration: AppExtensionProcess.Configuration) async throws](appextensionprocess/init(configuration:)-38zf.md)
  Finds an existing process for the specified app extension or creates a new one asynchronously.
- [AppExtensionProcess.Configuration](appextensionprocess/configuration.md)
  A structure that holds the identity of an app extension and process-related details.
### Connecting to the app extension
- [func makeXPCConnection() throws -> NSXPCConnection](appextensionprocess/makexpcconnection.md)
  Connect to the app extension process using the XPC types of the Foundation framework.
- [func makeXPCSession() throws -> XPCSession](appextensionprocess/makexpcsession.md)
  Connect to the app extension process using an XPC session.
### Invalidating the app-extension connection
- [func invalidate()](appextensionprocess/invalidate.md)
  Invalidates the host app’s connection to the app extension process.

## See Also

- [Discovering app extensions from your app](discovering-app-extensions-from-your-app.md)
  Find the app extensions that match your host app’s extension points and are available to use.
- [struct AppExtensionIdentity](appextensionidentity.md)
  A type that uniquely identifies an app extension on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess)*