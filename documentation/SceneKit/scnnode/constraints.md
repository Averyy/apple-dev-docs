# constraints

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A list of constraints affecting the node’s transformation.

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
var constraints: [SCNConstraint]? { get set }
```

```objc
@property (copy, nullable) NSArray<SCNConstraint *> * constraints;
```

## Discussion

An array of constraint objects. Before rendering, SceneKit evaluates all constraints attached to a node hierarchy and adjusts node transformations appropriately.

Use the [`SCNLookAtConstraint`](../scnlookatconstraint.md) class to make a node always point toward another node even as both are moved, or the [`SCNTransformConstraint`](../scntransformconstraint.md) class to apply arbitrary transformations at constraint evaluation time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/constraints)*