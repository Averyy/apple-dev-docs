# RotateGesture3D

**Framework**: SwiftUI  
**Kind**: struct

A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct RotateGesture3D
```

#### Overview

You can constrain this gesture to recognize rotation about a specific 3D axis. For example, `RotateGesture3D(constrainedToAxis: .x)` creates a gesture that recognizes rotation only around the global X axis. The axis you provide will be normalized.

A rotation gesture tracks how a rotation event sequence changes. To recognize a rotation gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:including:)`](view/gesture(_:including:).md) modifier.

## Topics

### Creating the gesture
- [init(constrainedToAxis: RotationAxis3D?, minimumAngleDelta: Angle)](rotategesture3d/init(constrainedtoaxis:minimumangledelta:).md)
  Creates a rotation gesture with a minimum delta for the gesture to start and axis to constrain measurement of rotation.
- [var minimumAngleDelta: Angle](rotategesture3d/minimumangledelta.md)
  The minimum angle delta before the gesture becomes active.
- [var constrainedAxis: RotationAxis3D?](rotategesture3d/constrainedaxis.md)
  An axis around which the rotation is constrained.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [func gesture(_:)](view/gesture(_:).md)
  Attaches an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](view/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](view/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](view/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [struct DragGesture](draggesture.md)
  A dragging motion that invokes an action as the drag-event sequence changes.
- [struct WindowDragGesture](windowdraggesture.md)
  A gesture that recognizes the motion of and handles dragging a window.
- [struct MagnifyGesture](magnifygesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotateGesture](rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct GestureMask](gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotategesture3d)*