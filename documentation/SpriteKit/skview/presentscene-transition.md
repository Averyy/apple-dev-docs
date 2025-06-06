# presentScene(_:transition:)

**Framework**: SpriteKit  
**Kind**: method

Transitions from the current scene to a new scene.

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
func presentScene(_ scene: SKScene, transition: SKTransition)
```

#### Discussion

If there is currently a scene presented by the view, the view’s [`scene`](skview/scene.md) property is updated immediately, the transition is executed to swap between the scenes. Otherwise, the new scene is presented immediately and the transition property is ignored.

## Parameters

- `scene`: The scene to present.
- `transition`: A transition used to animate between the two scenes.

## See Also

- [var scene: SKScene?](skview/scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene?)](skview/presentscene(_:).md)
  Presents a scene.
- [class SKTransition](sktransition.md)
  An object used to perform an animated transition to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:transition:))*