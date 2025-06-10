# EnvironmentBlendingComponent

**Framework**: RealityKit  
**Kind**: struct

A component which controls how an entity will blend visually with objects in the user’s local environment

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct EnvironmentBlendingComponent
```

## Topics

### Structures
- [EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/blendingmode.md)
  A struct that encapsulates the different environment-blending modes that can be applied to an entity
### Initializers
- [init()](environmentblendingcomponent/init.md)
  Creates an instance of the component using the `default` blending mode
- [init(preferredBlendingMode: EnvironmentBlendingComponent.BlendingMode)](environmentblendingcomponent/init(preferredblendingmode:).md)
  Creates an instance of the component
### Instance Properties
- [var preferredBlendingMode: EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/preferredblendingmode.md)
  Specifies how the entity and its descendants blend against environments which encompass them
### Enumerations
- [EnvironmentBlendingComponent.EnvironmentType](environmentblendingcomponent/environmenttype.md)
  An enumeration of the environment types which support environment-blending

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentblendingcomponent)*