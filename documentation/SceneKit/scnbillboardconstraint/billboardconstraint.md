# billboardConstraint

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new billboard constraint.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) billboardConstraint;
```

#### Return Value

A new billboard constraint object.

#### Discussion

A newly created constraint uses the [`all`](../scnbillboardaxis/all.md) type, so nodes affected by the constraint never rotate with respect to the scene’s point of view. Change the [`freeAxes`](./freeaxes.md) property to partially constrain a node’s orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/billboardconstraint)*