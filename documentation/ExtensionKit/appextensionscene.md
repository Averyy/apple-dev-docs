# AppExtensionScene

**Framework**: ExtensionKit  
**Kind**: protocol

An interface you use to provide a specific scene from your app extension’s UI.

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

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Overview

When your app extension provides custom UI, use this type to define a specific scene for that UI. An app extension can define multiple scene types in coordination with the host app. When the host app displays the app extension’s UI, it provides a unique string identifier for the scene it wants to display. The app extension responds by providing an instance of this type that contains that scene’s contents.

When defining a scene, provide the body of that scene using the [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) type. This type contains the unique identifier of the scene and the content to display. The following code shows an implementation of a scene capable of displaying content you supply at initialization time using a closure. The scene’s [`body`](appextensionscene/body-swift.property.md) property repackages that content inside the [`PrimitiveAppExtensionScene`](primitiveappextensionscene.md) structure. You can also use this type to accept a scene-specific XPC connection, which you might use to communicate custom data related to managing UI-related interactions.

```None
struct MyScene<Content: View>: AppExtensionScene {

    public init(content: @escaping () ->  Content) {
        self.content = content
    }

    private let content: () -> Content

    public var body: some AppExtensionScene {
        PrimitiveAppExtensionScene(id: “MyScene”) {
            content()
        } onConnection: { connection in
            // TODO: Configure the XPC connection and return true
            return false
        }
    }
}
```

For more information about creating UI-based app extensions, see [`Including extension-based UI in your interface`](including-extension-based-ui-in-your-interface.md).

## Topics

### Configuring the app extension
- [var body: Self.Body](appextensionscene/body-swift.property.md)
  The content and behavior of the scene’s interface.
- [associatedtype Body : AppExtensionScene](appextensionscene/body-swift.associatedtype.md)
  The type for this scene’s body.

## Relationships

### Conforming Types
- [PrimitiveAppExtensionScene](primitiveappextensionscene.md)

## See Also

- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A type you use to deliver the contents of your app-extension-based UI.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionscene)*