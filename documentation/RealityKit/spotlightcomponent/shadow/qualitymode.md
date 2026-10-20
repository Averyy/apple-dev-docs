# SpotLightComponent.Shadow.QualityMode

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Constants that select the shadow-filtering algorithm a spotlight uses.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS
- visionOS 27.0+

## Declaration

```swift
struct QualityMode
```

#### Overview

[`low`](./qualitymode/low.md) produces a hard-edged shadow with a uniform width. The shadow ignores [`lightSize`](./lightsize.md) and the distance between the light, the shadow-casting geometry, and the receiving surface.

[`medium`](./qualitymode/medium.md) and [`high`](./qualitymode/high.md) produce *soft* shadows whose penumbra widens as the receiving surface moves farther from the caster, approximating the appearance of an area light. [`high`](./qualitymode/high.md) takes more samples per pixel than [`medium`](./qualitymode/medium.md), producing a smoother penumbra at greater GPU cost.

## Topics

### Choosing a quality level
- [static var low: SpotLightComponent.Shadow.QualityMode](./qualitymode/low.md)
- [static var medium: SpotLightComponent.Shadow.QualityMode](./qualitymode/medium.md)
### Initializers
- [init(rawValue: Int)](./qualitymode/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: Int](./qualitymode/rawvalue.md)
### Type Properties
- [static var high: SpotLightComponent.Shadow.QualityMode](./qualitymode/high.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring shadow quality
- [var quality: SpotLightComponent.Shadow.QualityMode](./quality.md)
  The shadow-filtering algorithm this light uses.
- [var lightSize: Float](./lightsize.md)
  The radius of the spotlight’s emitting surface, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/qualitymode)*