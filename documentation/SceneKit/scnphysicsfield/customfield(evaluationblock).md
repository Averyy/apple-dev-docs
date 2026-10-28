# customField(evaluationBlock:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a field that runs the specified block to determine the force a field applies to each object in its area of effect.

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
class func customField(evaluationBlock block: @escaping SCNFieldForceEvaluator) -> SCNPhysicsField
```

```objc
+ (SCNPhysicsField *) customFieldWithEvaluationBlock:(SCNFieldForceEvaluator) block;
```

## Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](../scnnode/physicsfield.md) property of an [`SCNNode`](../scnnode.md) object.

## Discussion

For custom physics fields, SceneKit ignores the [`direction`](./direction.md), [`strength`](./strength.md), [`falloffExponent`](./falloffexponent.md), and [`minimumDistance`](./minimumdistance.md) properties. Instead, SceneKit calls your block to determine the direction and magnitude of force to apply to each physics body or particle in the field’s area of effect.

## Parameters

- `block`: A block that SceneKit runs for each object in the field’s area of effect. See [`SCNFieldForceEvaluator`](../scnfieldforceevaluator.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/customfield(evaluationblock:))*