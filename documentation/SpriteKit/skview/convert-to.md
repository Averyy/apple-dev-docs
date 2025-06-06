# convert(_:to:)

**Framework**: SpriteKit  
**Kind**: method

Converts a point from view coordinates to scene coordinates.

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
func convert(_ point: CGPoint, to scene: SKScene) -> CGPoint
```

#### Return Value

The same point in the scene’s coordinate system.

#### Discussion

This method performs the coordinate conversion as if the scene is presented inside the view.

## Parameters

- `point`: A point in view coordinates.
- `scene`: A scene.

## See Also

- [func convert(CGPoint, from: SKScene) -> CGPoint](skview/convert(_:from:).md)
  Converts a point from scene coordinates to view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/convert(_:to:))*