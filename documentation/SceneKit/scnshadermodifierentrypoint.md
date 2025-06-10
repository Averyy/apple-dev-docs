# SCNShaderModifierEntryPoint

**Framework**: SceneKit  
**Kind**: struct

Keys for the [`shaderModifiers`](scnshadable/shadermodifiers.md) dictionary, each corresponding to an entry point in SceneKit’s shader programs where you can attach a custom GPU shader code snippet.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct SCNShaderModifierEntryPoint
```

#### Discussion

For details on shader modifiers, see [`Use Shader Modifiers to Extend SceneKit Shading`](scnshadable#Use-Shader-Modifiers-to-Extend-SceneKit-Shading.md) in the protocol overview.

SceneKit inserts your shader modifiers into its shader program in the order shown here, so you can use the structures defined by earlier entry points in later entry points. For example, a snippet associated with the [`fragment`](scnshadermodifierentrypoint/fragment.md) entry point can read from the `_surface` structure defined by the [`surface`](scnshadermodifierentrypoint/surface.md) entry point.

## Topics

### Type Properties
- [static let fragment: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/fragment.md)
  Use this entry point to change the color of a fragment after all other shading has been performed.
- [static let geometry: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/geometry.md)
  Use this entry point to deform a geometry’s surface or alter its vertex attributes.
- [static let lightingModel: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/lightingmodel.md)
  Use this entry point to provide a custom lighting equation.
- [static let surface: SCNShaderModifierEntryPoint](scnshadermodifierentrypoint/surface.md)
  Use this entry point to modify the surface properties of a material before lighting is computed.
### Initializers
- [init(rawValue: String)](scnshadermodifierentrypoint/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias SCNBindingBlock](scnbindingblock.md)
  The signature for a block called for binding or unbinding a GLSL symbol in a custom program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadermodifierentrypoint)*