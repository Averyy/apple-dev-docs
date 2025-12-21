# ShaderGraphMaterial

**Framework**: RealityKit  
**Kind**: struct

A material that comes from a shader graph in a Reality Composer Pro project, or a MaterialX shader.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ShaderGraphMaterial
```

#### Overview

Use ShaderGraphMaterial when retrieving a shaders you build in Reality Composer Pro’s shader graph. The following code demonstrates retrieving the first material from an entity loaded from a Reality Composer Proj project and sets a new value for one of its named parameters:

```swift` if var modelComponent = entity.modelComponent { modelComponent.materials = modelComponent.materials.map { guard var material = $0 as? ShaderGraphMaterial else { return $0 } if material.parameterNames.contains(myMaterialParameterName) { do { try material.setParameter(name: myMaterialParameterName, value: .float(isPowered ? 1.0 : 0.0)) } catch { // Handle error. } } return material } entity.modelComponent = modelComponent }

```None

In addition to creating instances of `ShaderGraphMaterial` from Reality Composer Pro's shader graph, you can also create them directly from Material X shaders.

You can also load shader graph materials directly from `.reality` files:

```swift
let shader = try! await ShaderGraphMaterial(named: "/Root/Glass", from: "Scene.usda")
```

For more information on using custom parameters in a `ShaderGraphMaterial`,  see doc://documentation.apple.com/documentation/visionos/implementing-adjustable-material-in-visionos.

Create dynamic materials without Metal.

## Topics

### Shader Graph fundamentals
- [protocol Material](material.md)
  A type that describes the material aspects of a mesh, like color and texture.
- [struct MaterialParameterTypes](materialparametertypes.md)
  A set of types that material parameters can use.
### Initializers
- [init(materialXLabel: String, data: Data) async throws](shadergraphmaterial/init(materialxlabel:data:).md)
  Loads a ShaderGraphMaterial from MaterialX data.
- [init(named:from:)](shadergraphmaterial/init(named:from:).md)
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

## Relationships

### Conforms To
- [Material](material.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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