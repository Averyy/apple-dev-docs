# DragGesture

**Framework**: SwiftUI  
**Kind**: struct

A dragging motion that invokes an action as the drag-event sequence changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DragGesture
```

## Mentions

- [Composing SwiftUI gestures](composing-swiftui-gestures.md)

#### Overview

To recognize a drag gesture on a view, create and configure the gesture, and then add it to the view using the [`gesture(_:including:)`](view/gesture(_:including:).md) modifier.

Add a drag gesture to a [`Circle`](circle.md) and change its color while the user performs the drag gesture:

```swift
struct DragGestureView: View {
    @State private var isDragging = false

    var drag: some Gesture {
        DragGesture()
            .onChanged { _ in self.isDragging = true }
            .onEnded { _ in self.isDragging = false }
    }

    var body: some View {
        Circle()
            .fill(self.isDragging ? Color.red : Color.blue)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(drag)
    }
}
```

## Topics

### Creating a drag gesture
- [init(minimumDistance: CGFloat, coordinateSpace: some CoordinateSpaceProtocol)](draggesture/init(minimumdistance:coordinatespace:)-8ffe5.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
- [var minimumDistance: CGFloat](draggesture/minimumdistance.md)
  The minimum dragging distance before the gesture succeeds.
- [var coordinateSpace: CoordinateSpace](draggesture/coordinatespace.md)
  The coordinate space in which to receive location values.
### Deprecated initializers
- [init(minimumDistance: CGFloat, coordinateSpace: CoordinateSpace)](draggesture/init(minimumdistance:coordinatespace:)-3804h.md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.
### Structures
- [DragGesture.Value](draggesture/value.md)
  The attributes of a drag gesture.
### Initializers
- [init(minimumDistance:coordinateSpace:)](draggesture/init(minimumdistance:coordinatespace:).md)
  Creates a dragging gesture with the minimum dragging distance before the gesture succeeds and the coordinate space of the gesture’s location.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [func gesture(some UIGestureRecognizerRepresentable) -> some View](view/gesture(_:).md)
  Attaches a [`UIGestureRecognizerRepresentable`](uigesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](view/gesture(_:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](view/gesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](view/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture)*