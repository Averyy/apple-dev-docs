# semanticType

**Framework**: RealityKit  
**Kind**: property

The original type of this input.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let semanticType: ShaderGraph.NodeDefinition.SemanticType?
```

#### Discussion

Semantic types describe the type information from a standard, such as MaterialX 1.38. RealityKit converts this type information into a `ShaderGraph.DataType` on [`ShaderGraph.NodeLibrary`](shadergraph/nodelibrary.md) creation, which it can use for various type checking during ShaderGraphMaterial.Program compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/input/semantictype)*