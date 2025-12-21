# init(_:)

**Framework**: ExtensionKit  
**Kind**: init

Creates a scene configuration from a closure.

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
@preconcurrency init<Content>(_ content: @autoclosure @escaping @MainActor () -> Content) where Content : AppExtensionScene
```

#### Discussion

- content: The SwiftUI closure from which to build the scene’s content.

## See Also

- [init<Content, Configuration>(@autoclosure () -> Content, configuration: Configuration?)](appextensionsceneconfiguration/init(_:configuration:).md)
  Creates a scene configuration object from a closure and extension configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration/init(_:))*