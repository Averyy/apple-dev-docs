# MDLMaterialProperty

**Framework**: Model I/O  
**Kind**: class

A definition for one specific aspect of the rendering parameters for a material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMaterialProperty
```

#### Overview

The collection of material properties in a [`MDLMaterial`](mdlmaterial.md) instance defines the intended surface appearance for rendering a 3D object. A material property object’s [`semantic`](mdlmaterialproperty/semantic.md) property identifies which aspect of material rendering it affects, and its value (which can be any of several types) determines how the material property contributes to that aspect of rendering.

When you initialize a material property with a specific value (using one of the initializers listed in [`Creating a Material Property`](mdlmaterialproperty#Creating-a-Material-Property.md)) or set the value of an existing material property (using one of the property setters listed in [`Working with a Material Property’s Value`](mdlmaterialproperty#Working-with-a-Material-Propertys-Value.md)), the [`type`](mdlmaterialproperty/type.md) property changes to reflect the data type of the stored value. To retrieve the material property’s value, you must use the property accessor appropriate to its type. If you read a material property’s value using an accessor for a different type, the result is undefined.

## Topics

### Creating a Material Property
- [init(name: String, semantic: MDLMaterialSemantic)](mdlmaterialproperty/init(name:semantic:).md)
  Initializes a material property without a value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, string: String?)](mdlmaterialproperty/init(name:semantic:string:).md)
  Initializes a material property with a string value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, url: URL?)](mdlmaterialproperty/init(name:semantic:url:).md)
  Initializes a material property with a URL value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, textureSampler: MDLTextureSampler?)](mdlmaterialproperty/init(name:semantic:texturesampler:).md)
  Initializes a material property with a texture sampler object.
- [convenience init(name: String, semantic: MDLMaterialSemantic, color: CGColor)](mdlmaterialproperty/init(name:semantic:color:).md)
  Initializes a material property with a color value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float: Float)](mdlmaterialproperty/init(name:semantic:float:).md)
  Initializes a material property with a scalar value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float2: vector_float2)](mdlmaterialproperty/init(name:semantic:float2:).md)
  Initializes a material property with a 2-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float3: vector_float3)](mdlmaterialproperty/init(name:semantic:float3:).md)
  Initializes a material property with a 3-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, float4: vector_float4)](mdlmaterialproperty/init(name:semantic:float4:).md)
  Initializes a material property with a 4-component vector value.
- [convenience init(name: String, semantic: MDLMaterialSemantic, matrix4x4: matrix_float4x4)](mdlmaterialproperty/init(name:semantic:matrix4x4:).md)
  Initializes a material property with a 4 x 4 matrix value.
### Using a Material Property
- [var name: String](mdlmaterialproperty/name.md)
  A descriptive name for the material property.
- [var semantic: MDLMaterialSemantic](mdlmaterialproperty/semantic.md)
  The semantic meaning for the material property’s value.
- [var type: MDLMaterialPropertyType](mdlmaterialproperty/type.md)
  The data type stored in the material property’s value.
### Working with a Material Property’s Value
- [var stringValue: String?](mdlmaterialproperty/stringvalue.md)
  The string value for the material.
- [var urlValue: URL?](mdlmaterialproperty/urlvalue.md)
  The URL value for the material property—typically, the URL to a texture image.
- [var textureSamplerValue: MDLTextureSampler?](mdlmaterialproperty/texturesamplervalue.md)
  A texture sampler object that provides the texture image value for the material property.
- [var color: CGColor?](mdlmaterialproperty/color.md)
  The color value for the material property.
- [var floatValue: Float](mdlmaterialproperty/floatvalue.md)
  The scalar floating-point value for the material property.
- [var float2Value: vector_float2](mdlmaterialproperty/float2value.md)
  The 2-component floating-point vector value for the material property.
- [var float3Value: vector_float3](mdlmaterialproperty/float3value.md)
  The 3-component floating-point vector value for the material property.
- [var float4Value: vector_float4](mdlmaterialproperty/float4value.md)
  The 4-component floating-point vector value for the material property.
- [var matrix4x4: matrix_float4x4](mdlmaterialproperty/matrix4x4.md)
  The 4 x 4 floating-point matrix value for the material property.
### Copying a Material Property
- [func setProperties(MDLMaterialProperty)](mdlmaterialproperty/setproperties(_:).md)
  Sets the material property’s attributes to those of the specified material property.
### Constants
- [enum MDLMaterialSemantic](mdlmaterialsemantic.md)
  Options for the semantic use of a material property’s value in rendering a particular surface appearance; used by the [`semantic`](mdlmaterialproperty/semantic.md) property.
- [enum MDLMaterialPropertyType](mdlmaterialpropertytype.md)
  Options for the data type of a material property, used by the [`type`](mdlmaterialproperty/type.md) property.
### Instance Properties
- [var luminance: Float](mdlmaterialproperty/luminance.md)

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLMaterial](mdlmaterial.md)
  A collection of material properties that together describe the intended surface appearance for rendering a 3D object.
- [class MDLMaterialPropertyConnection](mdlmaterialpropertyconnection.md)
- [class MDLMaterialPropertyGraph](mdlmaterialpropertygraph.md)
- [class MDLMaterialPropertyNode](mdlmaterialpropertynode.md)
- [class MDLScatteringFunction](mdlscatteringfunction.md)
  A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.
- [class MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
  A set of material properties that describes a physically realistic shading model for materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty)*