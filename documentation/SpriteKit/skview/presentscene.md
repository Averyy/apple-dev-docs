# presentScene(_:)

**Framework**: SpriteKit  
**Kind**: method

Presents a scene.

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
func presentScene(_ scene: SKScene?)
```

## Mentions

- [Responding to Frame-Cycle Events](responding-to-frame-cycle-events.md)
- [Drawing SpriteKit Content in a View](drawing-spritekit-content-in-a-view.md)

#### Discussion

The new scene immediately replaces the current scene, if one exists.

## Parameters

- `scene`: The scene to present.

## See Also

- [var scene: SKScene?](skview/scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene, transition: SKTransition)](skview/presentscene(_:transition:).md)
  Transitions from the current scene to a new scene.
- [class SKTransition](sktransition.md)
  An object used to perform an animated transition to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/presentscene(_:))*