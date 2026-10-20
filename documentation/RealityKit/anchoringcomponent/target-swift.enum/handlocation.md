# AnchoringComponent.Target.HandLocation

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines the locations of tracked hands to look for.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct HandLocation
```

## Topics

### Structures
- [AnchoringComponent.Target.HandLocation.HandJoint](./handlocation/handjoint.md)
  Describes all the hand joints.
### Type Properties
- [static let aboveHand: AnchoringComponent.Target.HandLocation](./handlocation/abovehand.md)
  An anchor location above the center of the palm in the world space, regardless how the hand is rotated.
- [static let indexFingerTip: AnchoringComponent.Target.HandLocation](./handlocation/indexfingertip.md)
  An anchor location at the tip of the index finger.
- [static let palm: AnchoringComponent.Target.HandLocation](./handlocation/palm.md)
  An anchor location at the center of the palm.
- [static let thumbTip: AnchoringComponent.Target.HandLocation](./handlocation/thumbtip.md)
  An anchor location at the tip of the thumb.
- [static let wrist: AnchoringComponent.Target.HandLocation](./handlocation/wrist.md)
  An anchor location at the center of the wrist on the back of the hand.
### Type Methods
- [static func joint(for: AnchoringComponent.Target.HandLocation.HandJoint) -> AnchoringComponent.Target.HandLocation](./handlocation/joint%28for%29.md)
  The function that returns the `HandLocation` based on `HandJoint`.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Hand tracking
- [Happy Beam](../../../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [AnchoringComponent.Target.Chirality](./chirality.md)
  Defines the chirality of tracked hands to look for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/handlocation)*