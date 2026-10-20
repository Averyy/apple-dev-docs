# gesture(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Attaches an [`NSGestureRecognizerRepresentable`](../nsgesturerecognizerrepresentable.md) to the view.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func gesture(_ representable: some NSGestureRecognizerRepresentable) -> some View
```

**Other overloads**:

```swift
nonisolated
func gesture(_ representable: some UIGestureRecognizerRepresentable) -> some View
```

#### Return Value

A view with an [`NSGestureRecognizerRepresentable`](../nsgesturerecognizerrepresentable.md) attached.

## Parameters

- `representable`: The [`NSGestureRecognizerRepresentable`](../nsgesturerecognizerrepresentable.md) that creates and manages a gesture recognizer.

## See Also

### Recognizing gestures that change over time
- [func gesture<T>(T, isEnabled: Bool) -> some View](./gesture%28_,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](./gesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](./gesture%28_,including%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [struct DragGesture](../draggesture.md)
  A dragging motion that invokes an action as the drag-event sequence changes.
- [struct WindowDragGesture](../windowdraggesture.md)
  A gesture that recognizes the motion of and handles dragging a window.
- [struct MagnifyGesture](../magnifygesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotateGesture](../rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct RotateGesture3D](../rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [struct GestureMask](../gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gesture(_:))*