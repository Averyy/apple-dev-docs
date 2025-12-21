# init(id:content:onConnection:)

**Framework**: ExtensionKit  
**Kind**: init

Initializes the primitive app extension scene with the specified ID and closure for the content.

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
@preconcurrency init<Content>(id: String, @ViewBuilder content: @escaping () -> Content, onConnection: @escaping (NSXPCConnection) -> Bool = { _ in false }) where Content : View
```

#### Discussion

Use this method to initialize the type and provide the scene contents. The following example shows the typical code you use to create this type and specify its parameters. Replace the comments with the actual SwiftUI views and XPC connection code your app supports.

```None
public var body: some AppExtensionScene {
    PrimitiveAppExtensionScene(id: “MyScene”) {
        // SwiftUI views and behavior.
    } onConnection: { connection in
        // Configure the XPC connection and return true.
        return false
    }
}
```

For more information about creating scenes for your app extension, see [`Including extension-based UI in your interface`](including-extension-based-ui-in-your-interface.md).

## Parameters

- `id`: The unique identifier for this scene.
- `content`: A closure that provides the contents of the scene.
- `onConnection`: A closure that you use to accept a scene-specific XPC connection.   The closure returns a Boolean value that indicates whether you successfully completed   the connection. Return   if you successfully configured the XPC connection,   or   if you didn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene/init(id:content:onconnection:))*