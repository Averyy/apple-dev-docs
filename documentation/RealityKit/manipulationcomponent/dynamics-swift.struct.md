# ManipulationComponent.Dynamics

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Settings that allow customization of the interaction behavior per target.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Dynamics
```

## Topics

### Structures
- [ManipulationComponent.Dynamics.Inertia](./dynamics-swift.struct/inertia-swift.struct.md)
  The inertia of the object, related to the target’s mass. The larger the inertia, the less snappy the object is in response to user input.
- [ManipulationComponent.Dynamics.RotationBehavior](./dynamics-swift.struct/rotationbehavior.md)
  Definition of different standardized rotation behaviors for an object.
- [ManipulationComponent.Dynamics.ScalingBehavior](./dynamics-swift.struct/scalingbehavior-swift.struct.md)
  Definition of the two-handed scaling behavior.
- [ManipulationComponent.Dynamics.TranslationBehavior](./dynamics-swift.struct/translationbehavior-swift.struct.md)
  Definition of different standardized translation behaviors for an object.
### Initializers
- [init()](./dynamics-swift.struct/init%28%29.md)
### Instance Properties
- [var inertia: ManipulationComponent.Dynamics.Inertia](./dynamics-swift.struct/inertia-swift.property.md)
  How snappy the object’s movement is in response to input.
- [var primaryRotationBehavior: ManipulationComponent.Dynamics.RotationBehavior](./dynamics-swift.struct/primaryrotationbehavior.md)
  The rotation behavior describing how an object rotates due to pose changes from the primary input source, for example a single hand pose re-orienting.
- [var scalingBehavior: ManipulationComponent.Dynamics.ScalingBehavior](./dynamics-swift.struct/scalingbehavior-swift.property.md)
  The scaling behavior describing how an object scales due to gestures performed by the user.
- [var secondaryRotationBehavior: ManipulationComponent.Dynamics.RotationBehavior](./dynamics-swift.struct/secondaryrotationbehavior.md)
  The rotation behavior describing how an object rotates due to secondary input, for example two handed rotation.
- [var translationBehavior: ManipulationComponent.Dynamics.TranslationBehavior](./dynamics-swift.struct/translationbehavior-swift.property.md)
  The translation behavior describing how an object translates due to gestures performed by the user.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationcomponent/dynamics-swift.struct)*