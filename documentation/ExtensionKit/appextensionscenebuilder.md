# AppExtensionSceneBuilder

**Framework**: ExtensionKit  
**Kind**: struct

A custom parameter attribute that constructs extension scenes from closures.

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
@preconcurrency @resultBuilder struct AppExtensionSceneBuilder
```

## Topics

### Building the scene’s content
- [static func buildBlock<Content>(Content) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:).md)
  Passes through a single extension scene unmodified.
- [static func buildBlock<C0, C1>(C0, C1) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:).md)
  Builds an extension scene by combining two scenes.
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:).md)
  Builds an extension scene by combining three scenes.
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:).md)
  Builds an extension scene by combining four scenes.
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:).md)
  Builds an extension scene by combining five scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:_:).md)
  Builds an extension scene by combining six scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:_:_:).md)
  Builds an extension scene by combining seven scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:_:_:_:).md)
  Builds an extension scene by combining eight scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
  Builds an extension scene by combining nine scenes.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some AppExtensionScene](appextensionscenebuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
  Builds an extension scene by combining ten scenes.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AppExtensionScene](appextensionscene.md)
  An interface you use to provide a specific scene from your app extension’s UI.
- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A type you use to deliver the contents of your app-extension-based UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/appextensionscenebuilder)*