# GaussianSplatEvents

**Framework**: RealityKit  
**Kind**: enum

Events associated with Gaussian Splat component

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum GaussianSplatEvents
```

## Topics

### Structures
- [GaussianSplatEvents.RenderingChanged](gaussiansplatevents/renderingchanged.md)
  Clients may subscribe to this event to be notified of RealityKit taking measures to reduce the rendering impact of their GaussianSplatResource. The client can then choose how to respond. For example, they could switch to a lower splat count asset or reduce the total number of active SplatComponents in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatevents)*