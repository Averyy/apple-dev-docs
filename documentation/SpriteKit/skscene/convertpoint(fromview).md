# convertPoint(fromView:)

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
func convertPoint(fromView point: CGPoint) -> CGPoint
```

```objc
- (CGPoint) convertPointFromView:(CGPoint) point;
```

## Return Value

The same point in the scene’s coordinate system.

## Discussion

The scene must be presented in a view before calling this method.

## Parameters

- `point`: A point in view coordinates.

## See Also

### Converting Between Coordinate Systems
- [func convertPoint(toView: CGPoint) -> CGPoint](./convertpoint%28toview%29.md)
  Converts a point from scene coordinates to view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/convertpoint(fromview:))*