# init(scene:transition:isPaused:preferredFramesPerSecond:options:shouldRender:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@preconcurrency
nonisolated init(scene: SKScene, transition: SKTransition? = nil, isPaused: Bool = false, preferredFramesPerSecond: Int = 60, options: SpriteView.Options = [.shouldCullNonVisibleNodes], shouldRender: @escaping @MainActor (TimeInterval) -> Bool = { _ in true })
```

## See Also

### Creating a Sprite View
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int)](./init%28scene,transition,ispaused,preferredframespersecond%29.md)
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int, options: SpriteView.Options, debugOptions: SpriteView.DebugOptions, shouldRender: (TimeInterval) -> Bool)](./init%28scene,transition,ispaused,preferredframespersecond,options,debugoptions,shouldrender%29.md)
- [SpriteView.Options](./options.md)
- [SpriteView.DebugOptions](./debugoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/spriteview/init(scene:transition:ispaused:preferredframespersecond:options:shouldrender:))*