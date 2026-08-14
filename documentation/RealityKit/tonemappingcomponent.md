# ToneMappingComponent

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ToneMappingComponent
```

## Topics

### Creating a tone mapping component
- [init(exposure: Float, toeStrength: Float, toeLength: Float, shoulderStrength: Float, shoulderLength: Float, shoulderAngle: Float)](tonemappingcomponent/init(exposure:toestrength:toelength:shoulderstrength:shoulderlength:shoulderangle:).md)
  Initializes a `ToneMappingComponent` with the specified parameters. Values outside of their respective ranges are clamped.
### Configuring the tone curve
- [var exposure: Float](tonemappingcomponent/exposure.md)
  In F-stops
- [var toeStrength: Float](tonemappingcomponent/toestrength.md)
  As a ratio, clamped to [0.0, 1.0]
- [var toeLength: Float](tonemappingcomponent/toelength.md)
  As a ratio, clamped to [0.0, 1.0], where 1.0 means 50% of white point
- [var shoulderStrength: Float](tonemappingcomponent/shoulderstrength.md)
  In Fstops, clamped to [0.0, 10.0]
- [var shoulderLength: Float](tonemappingcomponent/shoulderlength.md)
  As a ratio, clamped to [0.0, 1.0]
- [var shoulderAngle: Float](tonemappingcomponent/shoulderangle.md)
  As a ratio, clamped to [0.0, 1.0]

## Relationships

### Conforms To
- [Component](component.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)

## See Also

- [struct BloomComponent](bloomcomponent.md)
  The `BloomComponent` adds a luminous glow effect around bright objects in the scene by extracting and blurring the brightest parts of the image, then combining them back with the original rendering. If scope is set to `unbounded` Bloom will be computed on the entire screen. If scope is set to `hierarchical` multiple Bloom Components can be used to opt in only the regions around certain objects for blooming.
- [struct BloomOptionsComponent](bloomoptionscomponent.md)
  A component that sets the properties for the bloom post-processing effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/tonemappingcomponent)*