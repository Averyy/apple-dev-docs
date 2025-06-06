# SCNFieldForceEvaluator

**Framework**: SceneKit  
**Kind**: typealias

The signature for a block that SceneKit calls to determine the effect of a custom field on an object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias SCNFieldForceEvaluator = (SCNVector3, SCNVector3, Float, Float, TimeInterval) -> SCNVector3
```

#### Discussion

You use this type of block to create a custom physics field with the [`customField(evaluationBlock:)`](scnphysicsfield/customfield(evaluationblock:).md) method. SceneKit calls your block once for each object in the field’s area of effect, on each step of the physics simulation.

> **Note**:  By default, one simulation step occurs for each frame rendered. For example, if your view renders at 60 frames per second and three bodies are in the field’s area of effect, SceneKit runs your block 180 times per second. To avoid reduced rendering performance, take care not to perform extensive computation in this block.

 By default, one simulation step occurs for each frame rendered. For example, if your view renders at 60 frames per second and three bodies are in the field’s area of effect, SceneKit runs your block 180 times per second. To avoid reduced rendering performance, take care not to perform extensive computation in this block.

The block takes the following parameters:

Your block uses these parameters to compute and return an [`SCNVector3`](scnvector3.md) force vector, which SceneKit then applies to the object affected by the field.

## See Also

- [enum SCNPhysicsFieldScope](scnphysicsfieldscope.md)
  Options for defining the region of space affected by a physics field, used by the [`scope`](scnphysicsfield/scope.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnfieldforceevaluator)*