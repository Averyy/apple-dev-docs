# MagnificationGesture

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A gesture that recognizes a magnification motion and tracks the amount of magnification.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: MagnifyGesture)
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: MagnifyGesture)
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: MagnifyGesture)
- macOS 10.15+ - Deprecated in 27.2 (renamed: MagnifyGesture)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: MagnifyGesture)

> **Deprecated**: Use [`MagnifyGesture`](./magnifygesture.md) instead.

## Declaration

```swift
nonisolated
struct MagnificationGesture
```

## Topics

### Creating the gesture
- [init(minimumScaleDelta: CGFloat)](./magnificationgesture/init%28minimumscaledelta%29.md)
  Creates a magnification gesture with a given minimum delta for the gesture to start.
- [var minimumScaleDelta: CGFloat](./magnificationgesture/minimumscaledelta.md)
  The minimum required delta before the gesture starts.

## Relationships

### Conforms To
- [Gesture](./gesture.md)

## See Also

### Deprecated
- [struct RotationGesture](./rotationgesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [func onTapGesture(count:coordinateSpace:perform:)](./view/ontapgesture%28count,coordinatespace,perform%29.md)
  Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/magnificationgesture)*