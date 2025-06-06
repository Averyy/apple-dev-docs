# PrimitiveAppExtensionScene

**Framework**: ExtensionKit  
**Kind**: struct

A primitive you use to compose specialized app extension points.

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
@preconcurrency struct PrimitiveAppExtensionScene
```

## Topics

### Creating an Extension Scene
- [init<Content>(id: String, content: () -> Content, onConnection: (NSXPCConnection) -> Bool)](primitiveappextensionscene/init(id:content:onconnection:).md)
  Creates a new app extension scene.
### Defining the Scene
- [var body: Never](primitiveappextensionscene/body.md)
  The scene’s user interface.
- [var debugDescription: String](primitiveappextensionscene/debugdescription.md)
  A string that provides information about the scene.
### Default Implementations
- [CustomDebugStringConvertible Implementations](primitiveappextensionscene/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [AppExtensionScene](appextensionscene.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AppExtensionScene](appextensionscene.md)
  A protocol that defines the user interface for an application extension.
- [struct AppExtensionSceneConfiguration](appextensionsceneconfiguration.md)
  An object that holds configuration options for an extension scene.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene)*