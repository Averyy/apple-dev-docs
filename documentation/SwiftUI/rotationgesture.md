# RotationGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that recognizes a rotation motion and tracks the angle of the rotation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
struct RotationGesture
```

## Topics

### Creating the gesture
- [init(minimumAngleDelta: Angle)](rotationgesture/init(minimumangledelta:).md)
  Creates a rotation gesture with a minimum delta for the gesture to start.
- [var minimumAngleDelta: Angle](rotationgesture/minimumangledelta.md)
  The minimum delta required before the gesture succeeds.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [struct MagnificationGesture](magnificationgesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [func onTapGesture(count:coordinateSpace:perform:)](view/ontapgesture(count:coordinatespace:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotationgesture)*