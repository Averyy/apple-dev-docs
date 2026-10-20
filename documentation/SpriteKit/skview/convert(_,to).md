# convert(_:to:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Converts a point from view coordinates to scene coordinates.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func convert(_ point: CGPoint, to scene: SKScene) -> CGPoint
```

```objc
- (CGPoint) convertPoint:(CGPoint) point toScene:(SKScene *) scene;
```

#### Return Value

The same point in the scene’s coordinate system.

#### Discussion

This method performs the coordinate conversion as if the scene is presented inside the view.

## Parameters

- `point`: A point in view coordinates.
- `scene`: A scene.

## See Also

### Converting Between View and Scene Coordinates
- [func convert(CGPoint, from: SKScene) -> CGPoint](./convert%28_,from%29.md)
  Converts a point from scene coordinates to view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skview/convert(_:to:))*