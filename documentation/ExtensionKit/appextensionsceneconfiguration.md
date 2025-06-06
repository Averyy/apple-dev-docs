# AppExtensionSceneConfiguration

**Framework**: ExtensionKit  
**Kind**: struct

An object that holds configuration options for an extension scene.

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

## Topics

### Creating Configuration Files
- [init<Content>(@autoclosure () -> Content)](appextensionsceneconfiguration/init(_:).md)
  Creates a scene configuration from a closure.
- [init<Content, Configuration>(@autoclosure () -> Content, configuration: Configuration?)](appextensionsceneconfiguration/init(_:configuration:).md)
  Creates a scene configuration object from a closure and extension configuration.
### Managing the Connection
- [func accept(connection: NSXPCConnection) -> Bool](appextensionsceneconfiguration/accept(connection:).md)
  A closure the framework calls when a host tries to connect to this extension.

## Relationships

### Conforms To
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AppExtensionScene](appextensionscene.md)
  A protocol that defines the user interface for an application extension.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.
- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A primitive you use to compose specialized app extension points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration)*