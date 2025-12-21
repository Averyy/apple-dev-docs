# init(from:surfaceShader:geometryModifier:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom material from an existing material, surface shader, and geometry modifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(from material: any Material, surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier? = nil) throws
```

#### Discussion

Use this initializer to create a custom material with the same properties as another existing material, but with a geometry modifier and surface shader.

## Parameters

- `material`: The material from which to copy properties.
- `surfaceShader`: The surface shader function.
- `geometryModifier`: The geometry modifier shader function.

## See Also

- [init(from: any Material, geometryModifier: CustomMaterial.GeometryModifier) throws](custommaterial/init(from:geometrymodifier:).md)
  Creates a custom material from an existing material and a geometry modifier.
- [init(surfaceShader: CustomMaterial.SurfaceShader, geometryModifier: CustomMaterial.GeometryModifier?, lightingModel: CustomMaterial.LightingModel) throws](custommaterial/init(surfaceshader:geometrymodifier:lightingmodel:).md)
  Creates a custom material from a lighting model, surface shader, and geometry modifier.
- [init(program: CustomMaterial.Program)](custommaterial/init(program:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/init(from:surfaceshader:geometrymodifier:))*