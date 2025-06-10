# HasAnchoring

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables anchoring of virtual content to a real-world object in an AR scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasAnchoring : Entity
```

## Topics

### Getting the component
- [var anchoring: AnchoringComponent](hasanchoring/anchoring.md)
  The component that describes how the virtual content is anchored to the real world.
### Identifying the AR anchor
- [var anchorIdentifier: UUID?](hasanchoring/anchoridentifier.md)
  The identifier of the AR anchor with which the anchor entity is associated, or `nil` if it isn’t currently anchored.
### Moving the anchor
- [func reanchor(AnchoringComponent.Target, preservingWorldTransform: Bool)](hasanchoring/reanchor(_:preservingworldtransform:).md)
  Changes the entity’s anchoring, preserving either the world transform or the local transform.

## Relationships

### Inherits From
- [Entity](entity.md)
### Conforming Types
- [AnchorEntity](anchorentity.md)

## See Also

- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [struct ARKitAnchorComponent](arkitanchorcomponent.md)
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasanchoring)*