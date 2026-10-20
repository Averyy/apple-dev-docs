# GestureMask

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct GestureMask
```

## Topics

### Getting gesture options
- [static let all: GestureMask](./gesturemask/all.md)
  Enable both the added gesture as well as all other gestures on the view and its subviews.
- [static let gesture: GestureMask](./gesturemask/gesture.md)
  Enable the added gesture but disable all gestures in the subview hierarchy.
- [static let subviews: GestureMask](./gesturemask/subviews.md)
  Enable all gestures in the subview hierarchy but disable the added gesture.
- [static let none: GestureMask](./gesturemask/none.md)
  Disable all gestures in the subview hierarchy, including the added gesture.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Recognizing gestures that change over time
- [func gesture(_:)](./view/gesture%28_%29.md)
  Attaches an [`NSGestureRecognizerRepresentable`](./nsgesturerecognizerrepresentable.md) to the view.
- [func gesture<T>(T, isEnabled: Bool) -> some View](./view/gesture%28_,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, name: String, isEnabled: Bool) -> some View](./view/gesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func gesture<T>(T, including: GestureMask) -> some View](./view/gesture%28_,including%29.md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [struct DragGesture](./draggesture.md)
  A dragging motion that invokes an action as the drag-event sequence changes.
- [struct WindowDragGesture](./windowdraggesture.md)
  A gesture that recognizes the motion of and handles dragging a window.
- [struct MagnifyGesture](./magnifygesture.md)
  A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [struct RotateGesture](./rotategesture.md)
  A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [struct RotateGesture3D](./rotategesture3d.md)
  A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturemask)*