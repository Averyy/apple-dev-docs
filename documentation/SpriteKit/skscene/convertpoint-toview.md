# convertPoint(toView:)

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
func convertPoint(toView point: CGPoint) -> CGPoint
```

#### Return Value

The same point in the view’s coordinate system.

#### Discussion

The scene must be presented in a view before calling this method.

## Parameters

- `point`: A point in scene coordinates.

## See Also

- [func convertPoint(fromView: CGPoint) -> CGPoint](skscene/convertpoint(fromview:).md)
  Converts a point from view coordinates to scene coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/convertpoint(toview:))*