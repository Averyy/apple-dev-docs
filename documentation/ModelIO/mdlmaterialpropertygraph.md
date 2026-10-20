# MDLMaterialPropertyGraph

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMaterialPropertyGraph
```

```objc
@interface MDLMaterialPropertyGraph : MDLMaterialPropertyNode
```

## Topics

### Initializers
- [init(nodes: [MDLMaterialPropertyNode], connections: [MDLMaterialPropertyConnection])](./mdlmaterialpropertygraph/init%28nodes,connections%29.md)
### Instance Properties
- [var connections: [MDLMaterialPropertyConnection]](./mdlmaterialpropertygraph/connections.md)
- [var nodes: [MDLMaterialPropertyNode]](./mdlmaterialpropertygraph/nodes.md)
### Instance Methods
- [func evaluate()](./mdlmaterialpropertygraph/evaluate%28%29.md)

## Relationships

### Inherits From
- [MDLMaterialPropertyNode](./mdlmaterialpropertynode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MDLNamed](./mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Materials
- [class MDLMaterial](./mdlmaterial.md)
  A collection of material properties that together describe the intended surface appearance for rendering a 3D object.
- [class MDLMaterialProperty](./mdlmaterialproperty.md)
  A definition for one specific aspect of the rendering parameters for a material.
- [class MDLMaterialPropertyConnection](./mdlmaterialpropertyconnection.md)
- [class MDLMaterialPropertyNode](./mdlmaterialpropertynode.md)
- [class MDLScatteringFunction](./mdlscatteringfunction.md)
  A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.
- [class MDLPhysicallyPlausibleScatteringFunction](./mdlphysicallyplausiblescatteringfunction.md)
  A set of material properties that describes a physically realistic shading model for materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph)*