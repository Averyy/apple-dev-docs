# init(scene:transition:isPaused:preferredFramesPerSecond:options:shouldRender:)

**Framework**: SpriteKit  
**Kind**: init

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
nonisolated init(scene: SKScene, transition: SKTransition? = nil, isPaused: Bool = false, preferredFramesPerSecond: Int = 60, options: SpriteView.Options = [.shouldCullNonVisibleNodes], shouldRender: @escaping @MainActor (TimeInterval) -> Bool = { _ in true })
```

## See Also

- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int)](spriteview/init(scene:transition:ispaused:preferredframespersecond:).md)
- [init(scene: SKScene, transition: SKTransition?, isPaused: Bool, preferredFramesPerSecond: Int, options: SpriteView.Options, debugOptions: SpriteView.DebugOptions, shouldRender: (TimeInterval) -> Bool)](spriteview/init(scene:transition:ispaused:preferredframespersecond:options:debugoptions:shouldrender:).md)
- [SpriteView.Options](spriteview/options.md)
- [SpriteView.DebugOptions](spriteview/debugoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/spriteview/init(scene:transition:ispaused:preferredframespersecond:options:shouldrender:))*