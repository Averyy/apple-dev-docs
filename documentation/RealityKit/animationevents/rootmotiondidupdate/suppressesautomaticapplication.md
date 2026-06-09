# suppressesAutomaticApplication

**Framework**: RealityKit  
**Kind**: property

Controls whether subscribing suppresses automatic root motion application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var suppressesAutomaticApplication: Bool { get nonmutating set }
```

#### Discussion

Defaults to `true` — the system will not apply root motion automatically when this event has subscribers. Set to `false` to allow automatic application even while observing the event.

> **Note**: This property only takes effect when using `scene.subscribe(to:on:)`. Changes made via `scene.publisher(for:on:)` are not written back to the engine.

## See Also

- [let rootMotionTransform: Transform](animationevents/rootmotiondidupdate/rootmotiontransform.md)
  The change in position and orientation since the previous frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate/suppressesautomaticapplication)*