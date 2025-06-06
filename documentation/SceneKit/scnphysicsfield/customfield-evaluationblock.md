# customField(evaluationBlock:)

**Framework**: SceneKit  
**Kind**: method

Creates a field that runs the specified block to determine the force a field applies to each object in its area of effect.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func customField(evaluationBlock block: @escaping SCNFieldForceEvaluator) -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

For custom physics fields, SceneKit ignores the [`direction`](scnphysicsfield/direction.md), [`strength`](scnphysicsfield/strength.md), [`falloffExponent`](scnphysicsfield/falloffexponent.md), and [`minimumDistance`](scnphysicsfield/minimumdistance.md) properties. Instead, SceneKit calls your block to determine the direction and magnitude of force to apply to each physics body or particle in the field’s area of effect.

## Parameters

- `block`: A block that SceneKit runs for each object in the field’s area of effect. See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/customfield(evaluationblock:))*