# manipulable(coordinateSpace:operations:inertia:isEnabled:onChanged:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Allows this view to be manipulated using common hand gestures.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@export(implementation)
nonisolated func manipulable(coordinateSpace: some CoordinateSpaceProtocol = .local, operations: Manipulable.Operation.Set = .all, inertia: Manipulable.Inertia = .medium, isEnabled: Bool = true, onChanged: ((Manipulable.Event) -> Void)? = nil) -> some View
```

#### Return Value

A view that can be manipulated using common hand gestures.

#### Discussion

When a person ends the manipulation gesture, the view will return to its initial transform from before the gesture began.

```swift
Model3D(named: "ToyRocket")
    .manipulable()
```

## Parameters

- `coordinateSpace`: The coordinate space of the manipulation gesture event locations.
- `operations`: The set of allowed operations that can be applied when a person manipulates this view.
- `inertia`: The inertia of this view that defines how much it resists being manipulated.
- `isEnabled`: The Boolean value that indicates whether the manipulation gesture added by this view modifier is enabled or not.
- `onChanged`: The action to perform with each new manipulation gesture event.

## See Also

### Hand interactions
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](./handgestureshortcut%28_,isenabled%29.md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](./handpointerbehavior%28_%29.md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./manipulable%28transform,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulable(using: Manipulable.GestureState) -> some View](./manipulable%28using%29.md)
  Allows the view to be manipulated using a manipulation gesture attached to a different view.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/manipulable(coordinatespace:operations:inertia:isenabled:onchanged:))*