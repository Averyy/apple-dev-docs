# AppExtensionSceneConfiguration

**Framework**: ExtensionKit  
**Kind**: struct

An object you use to configure an app extension that provides a custom UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AppExtensionSceneConfiguration
```

#### Overview

Use this type to provide the configuration details for an [`AppExtension`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension) type when the corresponding app extension provides a custom UI.

## Topics

### Creating the configuration
- [init<Content>(@autoclosure () -> Content)](appextensionsceneconfiguration/init(_:).md)
  Creates a scene configuration from a closure.
- [init<Content, Configuration>(@autoclosure () -> Content, configuration: Configuration?)](appextensionsceneconfiguration/init(_:configuration:).md)
  Creates a scene configuration object from a closure and extension configuration.
### Accepting a connection to the host app
- [func accept(connection: NSXPCConnection) -> Bool](appextensionsceneconfiguration/accept(connection:).md)
  A closure the framework calls when a host tries to connect to this extension.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration)*