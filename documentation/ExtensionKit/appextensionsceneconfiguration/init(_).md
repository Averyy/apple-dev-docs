# init(_:)

**Framework**: ExtensionKit  
**Kind**: init  
**Role**: Initializer

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

## Discussion

- content: The SwiftUI closure from which to build the scene’s content.

## See Also

### Creating the configuration
- [init<Content, Configuration>(@autoclosure () -> Content, configuration: Configuration?)](./init%28_,configuration%29.md)
  Creates a scene configuration object from a closure and extension configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration/init(_:))*