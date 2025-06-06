# scene

**Framework**: SpriteKit  
**Kind**: property

The scene currently presented by this view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var scene: SKScene? { get }
```

## Mentions

- [Choosing a SpriteKit Scene Renderer](choosing-a-spritekit-scene-renderer.md)

#### Discussion

The default value is `nil`.

You call [`presentScene(_:)`](skview/presentscene(_:).md) to assign a value to this property.

## See Also

- [func presentScene(SKScene?)](skview/presentscene(_:).md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](skview/presentscene(_:transition:).md)
  Transitions from the current scene to a new scene.
- [class SKTransition](sktransition.md)
  An object used to perform an animated transition to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/scene)*