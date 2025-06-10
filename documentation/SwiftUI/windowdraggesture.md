# WindowDragGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that recognizes the motion of and handles dragging a window.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct WindowDragGesture
```

#### Overview

To recognize a window drag gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:isEnabled:)`](view/gesture(_:isenabled:).md) modifier. Consider also letting the gesture [`allowsWindowActivationEvents(_:)`](View/allowsWindowActivationEvents(_:).md) so that dragging the containing window works even when it’s inactive.

To add a window drag gesture to a [`Circle`](circle.md) and change its color while a user performs the window drag gesture:

```swift
struct MyView: View {
    @GestureState var isDraggingWindow = false

    var dragWindow: some Gesture {
        WindowDragGesture()
            .updating($isDraggingWindow) { _, state, _ in
                state = true
            }
    }

    var body: some View {
        Circle()
            .fill(isDraggingWindow ? Color.green : .blue)
            .frame(width: 50, height: 50)
            .gesture(dragWindow)
            .allowsWindowActivationEvents()
    }
}
```

## Topics

### Structures
- [WindowDragGesture.Value](windowdraggesture/value.md)
  The properties of a window drag gesture.
### Initializers
- [init()](windowdraggesture/init.md)
  Creates a window drag gesture.

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
- [struct MagnifyGesture](magnifygesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotateGesture](rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct RotateGesture3D](rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [struct GestureMask](gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowdraggesture)*