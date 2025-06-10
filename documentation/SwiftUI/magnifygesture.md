# MagnifyGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that recognizes a magnification motion and tracks the amount of magnification.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MagnifyGesture
```

#### Overview

A magnify gesture tracks how a magnification event sequence changes. To recognize a magnify gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:including:)`](view/gesture(_:including:).md) modifier.

Add a magnify gesture to a [`Circle`](circle.md) that changes its size while the user performs the gesture:

```swift
struct MagnifyGestureView: View {
    @GestureState private var magnifyBy = 1.0

    var magnification: some Gesture {
        MagnifyGesture()
            .updating($magnifyBy) { value, gestureState, transaction in
                gestureState = value.magnification
            }
    }

    var body: some View {
        Circle()
            .frame(width: 100, height: 100)
            .scaleEffect(magnifyBy)
            .gesture(magnification)
    }
}
```

## Topics

### Creating the gesture
- [init(minimumScaleDelta: CGFloat)](magnifygesture/init(minimumscaledelta:).md)
  Creates a magnify gesture with a given minimum delta for the gesture to start.
- [var minimumScaleDelta: CGFloat](magnifygesture/minimumscaledelta.md)
  The minimum required delta before the gesture starts.

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
- [struct RotateGesture](rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct RotateGesture3D](rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [struct GestureMask](gesturemask.md)
  Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/magnifygesture)*