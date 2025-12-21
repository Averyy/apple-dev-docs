# AppExtension

**Framework**: ExtensionFoundation  
**Kind**: protocol

An interface you use to declare the content, structure, and behavior of an app extension.

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
protocol AppExtension
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

This type provides the entry point for an app extension, and every app extension must have a concrete type that adopts it. When a host app launches an app extension, the system looks for an object that adopts this protocol. The protocol provides default implementations of the code required to run the app extension.

When adopting this protocol, implement the [`configuration`](appextension/configuration-swift.property.md) property and provide a type capable of establishing an XPC connection to the host app. If your app extension sends only data to the host app, and doesn’t provide a UI, provide a type that implements the [`AppExtensionConfiguration`](appextensionconfiguration.md) protocol. If your extension provides UI elements for the host app to display, instead provide an instance of the [`AppExtensionSceneConfiguration`](https://developer.apple.com/documentation/ExtensionKit/AppExtensionSceneConfiguration) type.

## Topics

### Creating an app extension
- [init()](appextension/init.md)
  Initializes the app extension and prepares it to run.
### Configuring the app extension
- [var configuration: Self.Configuration](appextension/configuration-swift.property.md)
  The configuration details for this app extension.
- [associatedtype Configuration : AppExtensionConfiguration](appextension/configuration-swift.associatedtype.md)
  A type that manages configuration data for an app extension.
### Running the main event loop
- [static func main() throws](appextension/main-5zfjx.md)
  The main entry point for an app extension that doesn’t present any UI.
- [static func main() throws](appextension/main-w0u9.md)
  The main entry point for an app extension that doesn’t present any UI.
### Instance Properties
- [var extensionPoint: AppExtensionPoint](appextension/extensionpoint.md)
### Type Aliases
- [AppExtension.Bind](appextension/bind.md)
- [AppExtension.Identifier](appextension/identifier.md)
- [AppExtension.Implementing](appextension/implementing.md)
### Default Implementations
- [AppExtension Implementations](appextension/appextension-implementations.md)

## See Also

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)
  Create an app extension to perform tasks in a separate process from a host app.
- [protocol AppExtensionConfiguration](appextensionconfiguration.md)
  An interface you use to configure the XPC connection in your app extension.
- [struct ConnectionHandler](connectionhandler.md)
  A type that contains a custom closure that handles incoming XPC connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension)*