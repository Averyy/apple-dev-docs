# GaussianSplatEvents.RenderingChanged

**Framework**: RealityKit  
**Kind**: struct

Clients may subscribe to this event to be notified of RealityKit taking measures to reduce the rendering impact of their GaussianSplatResource. The client can then choose how to respond. For example, they could switch to a lower splat count asset or reduce the total number of active SplatComponents in the scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderingChanged
```

## Topics

### Instance Properties
- [let entity: Entity](gaussiansplatevents/renderingchanged/entity.md)
- [let isRenderingLimited: Bool](gaussiansplatevents/renderingchanged/isrenderinglimited.md)
- [let renderingStatus: GaussianSplatEvents.RenderingChanged.Status](gaussiansplatevents/renderingchanged/renderingstatus.md)
### Enumerations
- [GaussianSplatEvents.RenderingChanged.Status](gaussiansplatevents/renderingchanged/status.md)

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatevents/renderingchanged)*