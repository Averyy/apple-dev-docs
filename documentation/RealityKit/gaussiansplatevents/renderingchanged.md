# GaussianSplatEvents.RenderingChanged

**Framework**: RealityKit  
**Kind**: struct

An event that signals the framework changed how it renders an entity’s splats to manage performance.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderingChanged
```

#### Overview

Subscribe to this event to learn when the framework throttles splat rendering. In response, you can reduce the workload yourself — for example, by switching to a lower-count asset or removing other splat components from the scene.

## Topics

### Instance Properties
- [let entity: Entity](gaussiansplatevents/renderingchanged/entity.md)
  The entity whose Gaussian splat rendering changed.
- [let isRenderingLimited: Bool](gaussiansplatevents/renderingchanged/isrenderinglimited.md)
  A Boolean value that indicates whether the framework is currently limiting the entity’s splat rendering.
- [let renderingStatus: GaussianSplatEvents.RenderingChanged.Status](gaussiansplatevents/renderingchanged/renderingstatus.md)
  The level of rendering the framework now applies to the entity’s splats.
### Enumerations
- [GaussianSplatEvents.RenderingChanged.Status](gaussiansplatevents/renderingchanged/status.md)
  The level of detail at which the framework renders an entity’s splats.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatevents/renderingchanged)*