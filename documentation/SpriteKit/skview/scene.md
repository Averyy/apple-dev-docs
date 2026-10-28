# scene

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The scene currently presented by this view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var scene: SKScene? { get }
```

```objc
@property (nonatomic, readonly, nullable) SKScene * scene;
```

## Mentions

- [Choosing a SpriteKit Scene Renderer](../choosing-a-spritekit-scene-renderer.md)

## Discussion

The default value is `nil`.

You call [`presentScene(_:)`](./presentscene%28_%29.md) to assign a value to this property.

## See Also

### Displaying a Scene
- [func presentScene(SKScene?)](./presentscene%28_%29.md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](./presentscene%28_,transition%29.md)
  Transitions from the current scene to a new scene.
- [class SKTransition](../sktransition.md)
  An object used to perform an animated transition to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/scene)*