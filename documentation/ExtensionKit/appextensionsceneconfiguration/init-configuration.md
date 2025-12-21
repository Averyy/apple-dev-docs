# init(_:configuration:)

**Framework**: ExtensionKit  
**Kind**: init

Creates a scene configuration object from a closure and extension configuration.

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
@preconcurrency init<Content, Configuration>(_ content: @autoclosure @escaping @MainActor () -> Content, configuration: Configuration? = nil) where Content : AppExtensionScene, Configuration : AppExtensionConfiguration
```

#### Discussion

To provide a user interface, the extension’s `configuration` must be an [`AppExtensionSceneConfiguration`](appextensionsceneconfiguration.md), which combines an [`AppExtensionScene`](appextensionscene.md) with an optional non-UI [`AppExtensionConfiguration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtensionConfiguration). The `configuration` value you pass manages global interprocess communications with the host process, while the `content` value defines the extension’s user interface.

## Parameters

- `content`: The SwiftUI closure from which to build the scene’s content.
- `configuration`: An optional extension configuration file.

## See Also

- [init<Content>(@autoclosure () -> Content)](appextensionsceneconfiguration/init(_:).md)
  Creates a scene configuration from a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration/init(_:configuration:))*