# environment

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The view’s background, lighting, and acoustic properties.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency var environment: ARView.Environment { get set }
```

## See Also

### Providing environmental context
- [var physicsOrigin: Entity?](./physicsorigin.md)
  The entity that defines the origin of the scene’s physics simulation.
- [var audioListener: Entity?](./audiolistener.md)
  The entity that defines the listener position and orientation for spatial audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.property)*