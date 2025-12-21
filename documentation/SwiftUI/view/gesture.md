# gesture(_:)

**Framework**: SwiftUI  
**Kind**: method

Attaches an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md) to the view.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func gesture(_ representable: some NSGestureRecognizerRepresentable) -> some View
```

#### Return Value

A view with an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md) attached.

## Parameters

- `representable`: The    that creates and manages a gesture recognizer.

## See Also

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
- [struct RotateGesture3D](rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [struct GestureMask](gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gesture(_:))*