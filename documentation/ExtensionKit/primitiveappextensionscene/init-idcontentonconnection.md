# init(id:content:onConnection:)

**Framework**: ExtensionKit  
**Kind**: init

Creates a new app extension scene.

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

## Parameters

- `id`: A unique identifier for the scene.
- `content`: The scene’s user interface.
- `onConnection`: A closure that runs when the extension connects to its host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene/init(id:content:onconnection:))*