# primvarMappings

**Framework**: RealityKit  
**Kind**: property

Maps primvar names used in this graph to texture coordinate channels.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var primvarMappings: [String : ShaderGraph.TextureCoordinate]
```

#### Discussion

Primvar nodes reference geometry data by name. Use this dictionary to specify which [`ShaderGraph.TextureCoordinate`](shadergraph/texturecoordinate.md) channel each name resolves to at render time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/primvarmappings)*