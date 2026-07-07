# BloomOptionsComponent

**Framework**: RealityKit  
**Kind**: struct

A component that sets the properties for the bloom post-processing effects.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BloomOptionsComponent
```

#### Overview

This component has no effect without a BloomComponent in your scene.

It’s best to maintain a single BloomOptionsComponent in your scene. If more than one BloomOptionsComponent exists in your scene, one will be chosen based on proximity to the camera and depth in the entity hierarchy.

## Topics

### Configuring the bloom effect
- [var strength: Float](bloomoptionscomponent/strength.md)
  The intensity of the bloom effect.
- [var threshold: Float](bloomoptionscomponent/threshold.md)
  The brightness threshold for bloom activation.
- [var blurRadius: Float](bloomoptionscomponent/blurradius.md)
  The width of the bloom blur kernel as a percentage of viewport height
### Initializers
- [init()](bloomoptionscomponent/init.md)
  Creates a Bloom Options Component with default settings.

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)

## See Also

- [struct BloomComponent](bloomcomponent.md)
  The `BloomComponent` adds a luminous glow effect around bright objects in the scene by extracting and blurring the brightest parts of the image, then combining them back with the original rendering. If scope is set to `unbounded` Bloom will be computed on the entire screen. If scope is set to `hierarchical` multiple Bloom Components can be used to opt in only the regions around certain objects for blooming.
- [struct ToneMappingComponent](tonemappingcomponent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomoptionscomponent)*