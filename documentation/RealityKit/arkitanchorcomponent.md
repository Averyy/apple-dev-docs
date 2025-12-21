# ARKitAnchorComponent

**Framework**: RealityKit  
**Kind**: struct

A component that exposes the backing ARKit data of an anchored entity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ARKitAnchorComponent
```

## Topics

### Instance Properties
- [var anchor: any Anchor](arkitanchorcomponent/anchor.md)
  represents the backing anchor on visionOS.
- [var arAnchor: ARAnchor](arkitanchorcomponent/aranchor.md)
  represents the backing anchor on iOS.

## Relationships

### Conforms To
- [Component](component.md)
- [TransientComponent](transientcomponent.md)

## See Also

- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct.md)
  Options for how an entity tracks its target anchor.
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arkitanchorcomponent)*