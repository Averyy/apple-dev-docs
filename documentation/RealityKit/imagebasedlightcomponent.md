# ImageBasedLightComponent

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageBasedLightComponent
```

## Topics

### Operators
- [static func == (ImageBasedLightComponent, ImageBasedLightComponent) -> Bool](imagebasedlightcomponent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(source: ImageBasedLightComponent.Source, intensityExponent: Float)](imagebasedlightcomponent/init(source:intensityexponent:).md)
### Instance Properties
- [var inheritsRotation: Bool](imagebasedlightcomponent/inheritsrotation.md)
  Whether the IBL inherit the rotation of the Entity
- [var intensityExponent: Float](imagebasedlightcomponent/intensityexponent.md)
  The intensity value of the probe An intensityExponent of 0 means using the diffuse/specular intensities as-is Otherwise the intensity is multiplied by 2^intensityExponent
- [var source: ImageBasedLightComponent.Source](imagebasedlightcomponent/source-swift.property.md)
  Image(s) of the lighting environment
### Enumerations
- [ImageBasedLightComponent.Source](imagebasedlightcomponent/source-swift.enum.md)
### Default Implementations
- [Component Implementations](imagebasedlightcomponent/component-implementations.md)
- [Equatable Implementations](imagebasedlightcomponent/equatable-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [ImageBasedLightComponent.Source](imagebasedlightcomponent/source-swift.enum.md)
- [struct ImageBasedLightReceiverComponent](imagebasedlightreceivercomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagebasedlightcomponent)*