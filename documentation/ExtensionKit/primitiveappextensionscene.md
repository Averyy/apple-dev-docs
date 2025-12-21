# PrimitiveAppExtensionScene

**Framework**: ExtensionKit  
**Kind**: struct

A type you use to deliver the contents of your app-extension-based UI.

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

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Overview

When defining an [`AppExtensionScene`](appextensionscene.md) type, provide a `PrimitiveAppExtensionScene` structure as the body of that type. This type facilitates the delivery of the scene’s UI views back to the host app for incorporation into the host view controller. When constructing this type, specify one of the defined scene identifiers that the host app supports.

For more information about creating scenes for your app extension, see [`Including extension-based UI in your interface`](including-extension-based-ui-in-your-interface.md).

## Topics

### Creating a primitive extension scene
- [init<Content>(id: String, content: () -> Content, onConnection: (NSXPCConnection) -> Bool)](primitiveappextensionscene/init(id:content:onconnection:).md)
  Initializes the primitive app extension scene with the specified ID and closure for the content.
### Defining the scene contents
- [var body: Never](primitiveappextensionscene/body.md)
  The scene’s user interface.
### Describing the scene
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AppExtensionScene](appextensionscene.md)
  An interface you use to provide a specific scene from your app extension’s UI.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene)*