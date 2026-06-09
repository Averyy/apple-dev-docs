# manipulable(transform:coordinateSpace:operations:inertia:isEnabled:onChanged:)

**Framework**: SwiftUI  
**Kind**: method

Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol = .local, operations: Manipulable.Operation.Set = .all, inertia: Manipulable.Inertia = .medium, isEnabled: Bool = true, onChanged: ((Manipulable.Event) -> Void)? = nil) -> some View
```

#### Return Value

A view with a 3D affine transform applied and that can be manipulated using common hand gestures.

#### Discussion

When a person ends the manipulation gesture, the view will maintain its transform but you may also modify it programmatically when the gesture is inactive.

In the following example, when a person ends manipulating the view, it will fade out and fade in again in its original location and unmodified transform:

```swift
struct FadeOutOnReleaseView: View {
    @State private var transform: AffineTransform3D = .identity
    @State private var opacity: CGFloat = 1

    var body: some View {
        Circle()
            .manipulable(transform: $transform) { event in
                switch event.phase {
                case .ended(let value):
                    withAnimation {
                        opacity = 0
                    } completion: {
                        transform = .identity
                        withAnimation { opacity = 1 }
                    }
                default:
                    break
                }
            }
            .opacity(opacity)
        }
    }
}
```

## Parameters

- `transform`: The binding to a 3D affine transform applied to the view and updated when a person is manipulating this view.
- `coordinateSpace`: The coordinate space of the manipulation gesture event locations.
- `operations`: The set of allowed operations that can be applied when a person manipulates this view.
- `inertia`: The inertia of this view that defines how much it resists being manipulated.
- `isEnabled`: The Boolean value that indicates whether the manipulation gesture added by this view modifier is enabled or not.
- `onChanged`: The action to perform with each new manipulation gesture event.

## See Also

- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](view/handpointerbehavior(_:).md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](view/manipulable(using:).md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](view/manipulationgesture(updating:coordinatespace:operations:inertia:isenabled:onchanged:).md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/manipulable(transform:coordinatespace:operations:inertia:isenabled:onchanged:))*