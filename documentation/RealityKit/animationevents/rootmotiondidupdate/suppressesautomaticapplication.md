# suppressesAutomaticApplication

**Framework**: RealityKit  
**Kind**: property

A Boolean value that controls whether subscribing to the event suppresses automatic application of the root motion delta.

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

The default value is `true` — while the event has subscribers, the system doesn’t apply the delta automatically and the subscriber takes over. Set to `false` to keep automatic application in place while still observing the event.

> **Note**: This property only takes effect when subscribing through `scene.subscribe(to:on:)`. Changes made via `scene.publisher(for:on:)` aren’t written back to the engine.

## See Also

- [let rootMotionTransform: Transform](animationevents/rootmotiondidupdate/rootmotiontransform.md)
  The change in position and orientation since the previous frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate/suppressesautomaticapplication)*