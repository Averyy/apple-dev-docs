# LowLevelRendererError

**Framework**: RealityKit  
**Kind**: struct

An error thrown when creating or configuring a renderer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LowLevelRendererError
```

## Topics

### Describing the error
- [var errorDescription: String?](lowlevelrenderererror/errordescription.md)
  A human-readable description of the error.
- [var failureReason: String?](lowlevelrenderererror/failurereason.md)
  A human-readable explanation of why the error occurred.
- [var recoverySuggestion: String?](lowlevelrenderererror/recoverysuggestion.md)
  A human-readable suggestion for how to recover from the error.
- [var helpAnchor: String?](lowlevelrenderererror/helpanchor.md)
  A link to documentation for the error.
### Default Implementations
- [LocalizedError Implementations](lowlevelrenderererror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  The interface for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
  The interface for creating Metal shader functions from a ShaderGraph.
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown when binding or updating a low-level rendering resource fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderererror)*