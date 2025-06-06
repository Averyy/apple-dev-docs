# ShaderGraphMaterial

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct ShaderGraphMaterial
```

## Topics

### Initializers
- [init(materialXLabel: String, data: Data) async throws](shadergraphmaterial/init(materialxlabel:data:).md)
  Loads a ShaderGraphMaterial from MaterialX data.
- [init(named: String, from: URL) async throws](shadergraphmaterial/init(named:from:)-52t12.md)
  Loads a ShaderGraphMaterial from a url.
- [init(named: String, from: Data) async throws](shadergraphmaterial/init(named:from:)-9qt59.md)
  Loads a ShaderGraphMaterial from a named material within a USD file.
- [init(named: String, from: String, in: Bundle?) async throws](shadergraphmaterial/init(named:from:in:).md)
  Loads a ShaderGraphMaterial from a bundle.
### Instance Properties
- [var faceCulling: ShaderGraphMaterial.FaceCulling](shadergraphmaterial/faceculling-swift.property.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var parameterNames: [String]](shadergraphmaterial/parameternames.md)
- [var readsDepth: Bool](shadergraphmaterial/readsdepth.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var triangleFillMode: ShaderGraphMaterial.TriangleFillMode](shadergraphmaterial/trianglefillmode-swift.property.md)
  The object that controls how RealityKit draws triangles.
- [var writesDepth: Bool](shadergraphmaterial/writesdepth.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
### Instance Methods
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](shadergraphmaterial/getparameter(handle:).md)
- [func getParameter(name: String) -> MaterialParameters.Value?](shadergraphmaterial/getparameter(name:).md)
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](shadergraphmaterial/setparameter(handle:value:).md)
- [func setParameter(name: String, value: MaterialParameters.Value) throws](shadergraphmaterial/setparameter(name:value:).md)
### Type Aliases
- [ShaderGraphMaterial.FaceCulling](shadergraphmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [ShaderGraphMaterial.TriangleFillMode](shadergraphmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
### Type Methods
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](shadergraphmaterial/parameterhandle(name:).md)
### Enumerations
- [ShaderGraphMaterial.Error](shadergraphmaterial/error.md)
- [ShaderGraphMaterial.LoadError](shadergraphmaterial/loaderror.md)
### Default Implementations
- [Material Implementations](shadergraphmaterial/material-implementations.md)

## Relationships

### Conforms To
- [Material](material.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ShaderGraphMaterial.FaceCulling](shadergraphmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [ShaderGraphMaterial.TriangleFillMode](shadergraphmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)
  Write Metal shader functions to implement custom rendering effects.
- [struct CustomMaterial](custommaterial.md)
  A material that works with custom Metal shader functions.
- [CustomMaterial.SurfaceShader](custommaterial/surfaceshader.md)
  The custom material’s surface shader function.
- [CustomMaterial.GeometryModifier](custommaterial/geometrymodifier.md)
  The custom material’s optional shader function that can manipulate an entity’s vertex data.
- [protocol MaterialFunction](materialfunction.md)
  The abstract superclass for objects representing compute functions for RealityKit custom materials .
- [CustomMaterial.Program](custommaterial/program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](customshaderstage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial)*