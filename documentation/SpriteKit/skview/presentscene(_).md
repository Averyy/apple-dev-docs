# presentScene(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Presents a scene.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func presentScene(_ scene: SKScene?)
```

```objc
- (void) presentScene:(SKScene *) scene;
```

## Mentions

- [Drawing SpriteKit Content in a View](../drawing-spritekit-content-in-a-view.md)
- [Responding to Frame-Cycle Events](../responding-to-frame-cycle-events.md)

#### Discussion

The new scene immediately replaces the current scene, if one exists.

## Parameters

- `scene`: The scene to present.

## See Also

### Displaying a Scene
- [var scene: SKScene?](./scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene, transition: SKTransition)](./presentscene%28_,transition%29.md)
  Transitions from the current scene to a new scene.
- [class SKTransition](../sktransition.md)
  An object used to perform an animated transition to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:))*