# AppExtensionScene

**Framework**: ExtensionKit  
**Kind**: protocol

A protocol that defines the user interface for an application extension.

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
@preconcurrency protocol AppExtensionScene
```

## Topics

### Configuring the App Extension
- [var body: Self.Body](appextensionscene/body-swift.property.md)
  The content and behavior of the scene’s user interface.
- [associatedtype Body : AppExtensionScene](appextensionscene/body-swift.associatedtype.md)
  The type for this scene’s body.

## Relationships

### Conforming Types
- [PrimitiveAppExtensionScene](primitiveappextensionscene.md)

## See Also

- [struct AppExtensionSceneConfiguration](appextensionsceneconfiguration.md)
  An object that holds configuration options for an extension scene.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.
- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A primitive you use to compose specialized app extension points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionscene)*