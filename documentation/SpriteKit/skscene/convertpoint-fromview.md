# convertPoint(fromView:)

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
func convertPoint(fromView point: CGPoint) -> CGPoint
```

#### Return Value

The same point in the scene’s coordinate system.

#### Discussion

The scene must be presented in a view before calling this method.

## Parameters

- `point`: A point in view coordinates.

## See Also

- [func convertPoint(toView: CGPoint) -> CGPoint](skscene/convertpoint(toview:).md)
  Converts a point from scene coordinates to view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/convertpoint(fromview:))*