# isPaused

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to run actions, animations, particle systems, and physics simulations in the scene graph.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

#### Discussion

If [`false`](../../Swift/false.md) (the default), SceneKit continuously updates and renders the contents of the scene. Pausing a scene pauses any running animations or actions attached to the scene graph, and suspends updates of the scene’s physics simulation and any particle systems in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscene/ispaused)*