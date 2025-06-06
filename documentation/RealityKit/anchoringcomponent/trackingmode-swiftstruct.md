# AnchoringComponent.TrackingMode

**Framework**: RealityKit  
**Kind**: struct

Decides how the `Entity` tracks its target anchor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct TrackingMode
```

## Topics

### Operators
- [static func == (AnchoringComponent.TrackingMode, AnchoringComponent.TrackingMode) -> Bool](anchoringcomponent/trackingmode-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](anchoringcomponent/trackingmode-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anchoringcomponent/trackingmode-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let continuous: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct/continuous.md)
  Continuously anchors the entity to its target based on the target’s realtime location and hides the entity when the target is no longer in frame.
- [static let once: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct/once.md)
  Anchors the entity to the target on the first frame the target is found.
- [static let predicted: AnchoringComponent.TrackingMode](anchoringcomponent/trackingmode-swift.struct/predicted.md)
  Continuously anchors the entity to its target based on the target’s predicted location and hides the entity when the target is no longer in frame.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/trackingmode-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/trackingmode-swift.struct)*