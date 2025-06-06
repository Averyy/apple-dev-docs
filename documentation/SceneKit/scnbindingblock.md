# SCNBindingBlock

**Framework**: SceneKit  
**Kind**: typealias

The signature for a block called for binding or unbinding a GLSL symbol in a custom program.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNBindingBlock = (UInt32, UInt32, SCNNode?, SCNRenderer) -> Void
```

#### Discussion

The block takes the following parameters:

Call [`handleBinding(ofSymbol:handler:)`](scnshadable/handlebinding(ofsymbol:handler:).md) or [`handleUnbinding(ofSymbol:handler:)`](scnshadable/handleunbinding(ofsymbol:handler:).md) to associate a handler block with a GLSL symbol for a SceneKit geometry or material.

## See Also

- [struct SCNShaderModifierEntryPoint](scnshadermodifierentrypoint.md)
  Keys for the [`shaderModifiers`](scnshadable/shadermodifiers.md) dictionary, each corresponding to an entry point in SceneKit’s shader programs where you can attach a custom GPU shader code snippet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbindingblock)*