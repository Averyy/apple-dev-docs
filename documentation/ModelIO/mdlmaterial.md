# MDLMaterial

**Framework**: Model I/O  
**Kind**: class

A collection of material properties that together describe the intended surface appearance for rendering a 3D object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMaterial
```

#### Overview

Each material property (a [`MDLMaterialProperty`](mdlmaterialproperty.md) object) provides one specific aspect of appearance, such as opacity, shininess, or surface detail. Use the [`material`](mdlsubmesh/material.md) property of a [`MDLSubmesh`](mdlsubmesh.md) object to associate a material with a 3D object for rendering or to find the material assigned to an object loaded from an asset file.

Sets of certain material properties called  determine the material’s response to lighting. You can manage these properties together using a material’s [`scatteringFunction`](mdlmaterial/scatteringfunction.md) property. Creating a material with the inherited [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) initializer is equivalent to using the [`init(name:scatteringFunction:)`](mdlmaterial/init(name:scatteringfunction:).md) with a [`MDLScatteringFunction`](mdlscatteringfunction.md) object whose properties all have default values.

## Topics

### Creating a material
- [init(name: String, scatteringFunction: MDLScatteringFunction)](mdlmaterial/init(name:scatteringfunction:).md)
  Initializes a material
### Using a material
- [var materialFace: MDLMaterialFace](mdlmaterial/materialface.md)
  The surface of an object.
- [var name: String](mdlmaterial/name.md)
  A descriptive name for the material.
### Determining a material’s response to lighting
- [var scatteringFunction: MDLScatteringFunction](mdlmaterial/scatteringfunction.md)
  The collection of material properties that define the material’s response to light.
### Working with individual material properties
- [func propertyNamed(String) -> MDLMaterialProperty?](mdlmaterial/propertynamed(_:).md)
  Returns the material property with the specified name.
- [func property(with: MDLMaterialSemantic) -> MDLMaterialProperty?](mdlmaterial/property(with:).md)
  Returns the material property for the specified material semantic.
- [func properties(with: MDLMaterialSemantic) -> [MDLMaterialProperty]](mdlmaterial/properties(with:).md)
  Returns the complete list of material properties that match the specified material semantic.
- [func setProperty(MDLMaterialProperty)](mdlmaterial/setproperty(_:).md)
  Adds a new material property to or replaces an existing material property in the material.
- [func remove(MDLMaterialProperty)](mdlmaterial/remove(_:).md)
  Removes the specified material property from the material.
- [func removeAllProperties()](mdlmaterial/removeallproperties.md)
  Removes all material properties from the material.
### Sharing material properties
- [var base: MDLMaterial?](mdlmaterial/base.md)
  Another material object from which this material’s properties are derived.
### Accessing material properties with subscript syntax
- [subscript(String) -> MDLMaterialProperty?](mdlmaterial/subscript(_:)-323j3.md)
  Returns the material property with the specified name, for use with subscript syntax.
- [subscript(Int) -> MDLMaterialProperty?](mdlmaterial/subscript(_:)-19j2.md)
  Returns the material property at the specified index in the material, for use with subscript syntax.
- [var count: Int](mdlmaterial/count.md)
  The number of material properties in the material.
### Working with textures using resolvers
- [func loadTextures(using: any MDLAssetResolver)](mdlmaterial/loadtextures(using:).md)
  Loads textures using resolver for string paths and NSURLs.
- [func resolveTextures(with: any MDLAssetResolver)](mdlmaterial/resolvetextures(with:).md)
  Resolves all texture string paths as NSURLs with resolver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLMaterialProperty](mdlmaterialproperty.md)
  A definition for one specific aspect of the rendering parameters for a material.
- [class MDLMaterialPropertyConnection](mdlmaterialpropertyconnection.md)
- [class MDLMaterialPropertyGraph](mdlmaterialpropertygraph.md)
- [class MDLMaterialPropertyNode](mdlmaterialpropertynode.md)
- [class MDLScatteringFunction](mdlscatteringfunction.md)
  A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.
- [class MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
  A set of material properties that describes a physically realistic shading model for materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial)*