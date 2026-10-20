# RotationGesture

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A gesture that recognizes a rotation motion and tracks the angle of the rotation.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: RotateGesture)
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: RotateGesture)
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: RotateGesture)
- macOS 10.15+ - Deprecated in 27.2 (renamed: RotateGesture)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: RotateGesture)

> **Deprecated**: Use [`RotateGesture`](./rotategesture.md) instead.

## Declaration

```swift
nonisolated
struct RotationGesture
```

## Topics

### Creating the gesture
- [init(minimumAngleDelta: Angle)](./rotationgesture/init%28minimumangledelta%29.md)
  Creates a rotation gesture with a minimum delta for the gesture to start.
- [var minimumAngleDelta: Angle](./rotationgesture/minimumangledelta.md)
  The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To
- [Gesture](./gesture.md)

## See Also

### Deprecated
- [struct MagnificationGesture](./magnificationgesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [func onTapGesture(count:coordinateSpace:perform:)](./view/ontapgesture%28count,coordinatespace,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotationgesture)*