# AnchoringComponent.Target.HandLocation

**Framework**: RealityKit  
**Kind**: struct

Defines the locations of tracked hands to look for.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
struct HandLocation
```

## Topics

### Structures
- [AnchoringComponent.Target.HandLocation.HandJoint](anchoringcomponent/target-swift.enum/handlocation/handjoint.md)
  Describes all the hand joints.
### Operators
- [static func == (AnchoringComponent.Target.HandLocation, AnchoringComponent.Target.HandLocation) -> Bool](anchoringcomponent/target-swift.enum/handlocation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](anchoringcomponent/target-swift.enum/handlocation/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anchoringcomponent/target-swift.enum/handlocation/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let aboveHand: AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/abovehand.md)
  An anchor location above the center of the palm in the world space, regardless how the hand is rotated.
- [static let indexFingerTip: AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/indexfingertip.md)
  An anchor location at the tip of the index finger.
- [static let palm: AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/palm.md)
  An anchor location at the center of the palm.
- [static let thumbTip: AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/thumbtip.md)
  An anchor location at the tip of the thumb.
- [static let wrist: AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/wrist.md)
  An anchor location at the center of the wrist on the back of the hand.
### Type Methods
- [static func joint(for: AnchoringComponent.Target.HandLocation.HandJoint) -> AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation/joint(for:).md)
  The function that returns the `HandLocation` based on `HandJoint`.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/target-swift.enum/handlocation/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [AnchoringComponent.Target.Chirality](anchoringcomponent/target-swift.enum/chirality.md)
  Defines the chirality of tracked hands to look for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/handlocation)*