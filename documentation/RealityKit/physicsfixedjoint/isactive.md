# isActive

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the joint is active.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

Inactive joints do not participate in the physics simulation.

One example is a joint that does not reference any [`Entity`](entity.md) with [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md), or when one or both the referenced entities are not active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsfixedjoint/isactive)*