# targetEntity

**Framework**: RealityKit  
**Kind**: property

The root entity for the portal’s target world.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var targetEntity: Entity? { get set }
```

#### Discussion

When the target entity is valid and has a [`WorldComponent`](worldcomponent.md), the portal renders with the target entity and its hierarchy tree.

When the target entity doesn’t have a [`WorldComponent`](worldcomponent.md), the portal doesn’t render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/targetentity)*