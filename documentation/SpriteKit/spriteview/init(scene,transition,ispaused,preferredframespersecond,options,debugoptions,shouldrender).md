# init(scene:transition:isPaused:preferredFramesPerSecond:options:debugOptions:shouldRender:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
@preconcurrency
nonisolated init(scene: SKScene, transition: SKTransition? = nil, isPaused: Bool = false, preferredFramesPerSecond: Int = 60, options: SpriteView.Options = [.shouldCullNonVisibleNodes], debugOptions: SpriteView.DebugOptions, shouldRender: @escaping @MainActor (TimeInterval) -> Bool = { _ in true })
```

## See Also

### Creating a Sprite View
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int)](./init%28scene,transition,ispaused,preferredframespersecond%29.md)
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int, options: SpriteView.Options, shouldRender: (TimeInterval) -> Bool)](./init%28scene,transition,ispaused,preferredframespersecond,options,shouldrender%29.md)
- [SpriteView.Options](./options.md)
- [SpriteView.DebugOptions](./debugoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/spriteview/init(scene:transition:ispaused:preferredframespersecond:options:debugoptions:shouldrender:))*