# init(scene:transition:isPaused:preferredFramesPerSecond:options:debugOptions:shouldRender:)

**Framework**: SpriteKit  
**Kind**: init

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
nonisolated init(scene: SKScene, transition: SKTransition? = nil, isPaused: Bool = false, preferredFramesPerSecond: Int = 60, options: SpriteView.Options = [.shouldCullNonVisibleNodes], debugOptions: SpriteView.DebugOptions, shouldRender: @escaping @MainActor (TimeInterval) -> Bool = { _ in true })
```

## See Also

- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int)](spriteview/init(scene:transition:ispaused:preferredframespersecond:).md)
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int, options: SpriteView.Options, shouldRender: (TimeInterval) -> Bool)](spriteview/init(scene:transition:ispaused:preferredframespersecond:options:shouldrender:).md)
- [SpriteView.Options](spriteview/options.md)
- [SpriteView.DebugOptions](spriteview/debugoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/spriteview/init(scene:transition:ispaused:preferredframespersecond:options:debugoptions:shouldrender:))*