# SpotLightComponent.Shadow.QualityMode

**Framework**: RealityKit  
**Kind**: struct

Constants that select the shadow-filtering algorithm a spotlight uses.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct QualityMode
```

#### Overview

[`low`](spotlightcomponent/shadow/qualitymode/low.md) produces a hard-edged shadow with a uniform width. The shadow ignores [`lightSize`](spotlightcomponent/shadow/lightsize.md) and the distance between the light, the shadow-casting geometry, and the receiving surface.

[`medium`](spotlightcomponent/shadow/qualitymode/medium.md) and [`high`](spotlightcomponent/shadow/qualitymode/high.md) produce *soft* shadows whose penumbra widens as the receiving surface moves farther from the caster, approximating the appearance of an area light. [`high`](spotlightcomponent/shadow/qualitymode/high.md) takes more samples per pixel than [`medium`](spotlightcomponent/shadow/qualitymode/medium.md), producing a smoother penumbra at greater GPU cost.

## Topics

### Choosing a quality level
- [static var low: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/low.md)
- [static var medium: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/medium.md)
### Initializers
- [init(rawValue: Int)](spotlightcomponent/shadow/qualitymode/init(rawvalue:).md)
### Instance Properties
- [var rawValue: Int](spotlightcomponent/shadow/qualitymode/rawvalue.md)
### Type Properties
- [static var high: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/qualitymode/high.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var quality: SpotLightComponent.Shadow.QualityMode](spotlightcomponent/shadow/quality.md)
  The shadow-filtering algorithm this light uses.
- [var lightSize: Float](spotlightcomponent/shadow/lightsize.md)
  The radius of the spotlight’s emitting surface, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/qualitymode)*