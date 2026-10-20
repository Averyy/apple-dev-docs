# SCNFieldForceEvaluator

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for a block that SceneKit calls to determine the effect of a custom field on an object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
typealias SCNFieldForceEvaluator = (SCNVector3, SCNVector3, Float, Float, TimeInterval) -> SCNVector3
```

```c
typedef struct SCNVector3 (^)(struct SCNVector3, struct SCNVector3, float, float, double) SCNFieldForceEvaluator;
```

#### Discussion

You use this type of block to create a custom physics field with the [`customField(evaluationBlock:)`](./scnphysicsfield/customfield%28evaluationblock%29.md) method. SceneKit calls your block once for each object in the field’s area of effect, on each step of the physics simulation.

> **Note**:  By default, one simulation step occurs for each frame rendered. For example, if your view renders at 60 frames per second and three bodies are in the field’s area of effect, SceneKit runs your block 180 times per second. To avoid reduced rendering performance, take care not to perform extensive computation in this block.

The block takes the following parameters:

- **position**: The position of the object affected by the field, in the local coordinate space of the node containing the field.
- **velocity**: The velocity of the object affected by the field, relative to the local coordinate space of the node containing the field.
- **mass**: The mass of the object affected by the field. (See the [`mass`](./scnphysicsbody/mass.md) property for physics bodies and the [`particleMass`](./scnparticlesystem/particlemass.md) property for particle systems.)
- **charge**: The electrical charge of the object affected by the field. (See the [`charge`](./scnphysicsbody/charge.md) property for physics bodies and the [`particleCharge`](./scnparticlesystem/particlecharge.md) property for particle systems.)
- **time**: The elapsed time, in seconds, since the last simulation step.

Your block uses these parameters to compute and return an [`SCNVector3`](./scnvector3.md) force vector, which SceneKit then applies to the object affected by the field.

## See Also

### Constants
- [enum SCNPhysicsFieldScope](./scnphysicsfieldscope.md)
  Options for defining the region of space affected by a physics field, used by the [`scope`](./scnphysicsfield/scope.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfieldforceevaluator)*