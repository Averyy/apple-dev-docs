# init(engine:mesh:materials:)

**Framework**: PHASE  
**Kind**: init

Creates an object of a specific material that the given geometric data shapes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(engine: PHASEEngine, mesh: MDLMesh, materials: [PHASEMaterial])
```

#### Discussion

The framework assigns a material from the material array for every submesh in the mesh object. For example, PHASE infers that the first mesh is wooden if the first element of the material array is [`PHASEMaterialPreset.wood`](phasematerialpreset/wood.md).

If the number of submeshes within the mesh is less than or equal to the material array count, each material indexes the corresponding element. If the number of submeshes is greater than the material array count, each material indexes the element at the element index modulo the material count.

The framework generates an error for empty material arrays or `nil` array entries.

## Parameters

- `engine`: The object that controls this class’s associated audio output.
- `mesh`: A collection of points that connect to form a shape.
- `materials`: An array of objects that describe surface characteristics.

## See Also

- [init(engine: PHASEEngine, mesh: MDLMesh)](phaseshape/init(engine:mesh:).md)
  Creates an object that the given geometric data shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseshape/init(engine:mesh:materials:))*