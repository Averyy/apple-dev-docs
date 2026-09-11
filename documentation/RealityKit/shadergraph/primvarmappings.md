# primvarMappings

**Framework**: RealityKit  
**Kind**: property

Maps primvar names used in this graph to texture coordinate channels.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var primvarMappings: [String : ShaderGraph.TextureCoordinate]
```

#### Discussion

Primvar nodes reference geometry data by name. Use this dictionary to specify which [`ShaderGraph.TextureCoordinate`](shadergraph/texturecoordinate.md) channel each name resolves to at render time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/primvarmappings)*