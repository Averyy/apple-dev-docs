# HasAnchoring Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var anchorIdentifier: UUID?](anchorentity/anchoridentifier.md)
  The identifier of the AR anchor with which the anchor entity is associated, or `nil` if it isn’t currently anchored.
- [var anchoring: AnchoringComponent](anchorentity/anchoring.md)
  The component that describes how the virtual content is anchored to the real world.
### Instance Methods
- [func reanchor(AnchoringComponent.Target, preservingWorldTransform: Bool)](anchorentity/reanchor(_:preservingworldtransform:).md)
  Changes the entity’s anchoring, preserving either the world transform or the local transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchorentity/hasanchoring-implementations)*