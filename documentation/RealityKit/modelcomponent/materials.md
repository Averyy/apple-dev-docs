# materials

**Framework**: RealityKit  
**Kind**: property

The materials that define the model’s visual appearance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var materials: [any Material]
```

#### Discussion

Each [`MeshResource`](meshresource.md) requires a set of materials. An entity that has no materials renders using a magenta striped material. To determine the number of materials a mesh requires, use [`expectedMaterialCount`](meshresource/expectedmaterialcount.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelcomponent/materials)*