# convert(_:from:)

**Framework**: SpriteKit  
**Kind**: method

Converts a point from scene coordinates to view coordinates.

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
func convert(_ point: CGPoint, from scene: SKScene) -> CGPoint
```

#### Return Value

The same point in the view’s coordinate system.

#### Discussion

This method performs the coordinate conversion as if the scene is presented inside the view.

## Parameters

- `point`: A point in scene coordinates.
- `scene`: A scene.

## See Also

- [func convert(CGPoint, to: SKScene) -> CGPoint](skview/convert(_:to:).md)
  Converts a point from view coordinates to scene coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/convert(_:from:))*