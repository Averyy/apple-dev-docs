# manipulable(using:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Allows the view to be manipulated using a manipulation gesture attached to a different view.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
@export(implementation)
nonisolated func manipulable(using gestureState: Manipulable.GestureState) -> some View
```

## Return Value

A view that can be manipulated by a manipulation gesture attached to a different view.

## Discussion

Use this view modifier alongside [`manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)`](./manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md) when you want to allow a person to manipulate a view by interacting with a different view.

In the following example, a person can begin a manipulation gesture attached to a deck of cards which, in turn, manipulates a single card instead of the entire deck:

```swift
struct CardDeck: View {
    @State private var manipulationState = Manipulable.GestureState()

    var body: some View {
        ZStack {
            Model3D(named: "CardDeck")
                .manipulationGesture(updating: $manipulationState)
            Model3D(named: "Card")
                .manipulable(using: manipulationState)
                .opacity(manipulationState.isActive ? 1 : 0)
        }
    }
}
```

> **See Also**: [`manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)`](./manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md)

## Parameters

- `gestureState`: The manipulation gesture state that’s updated by a manipulation gesture added to a different view.

## See Also

### Hand interactions
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](./handgestureshortcut%28_,isenabled%29.md)
  Assigns a hand gesture shortcut to the modified control.
- [func handPointerBehavior(HandPointerBehavior?) -> some View](./handpointerbehavior%28_%29.md)
  Sets the behavior of the hand pointer while the user is interacting with the view.
- [func manipulable(coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./manipulable%28coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Allows this view to be manipulated using common hand gestures.
- [func manipulable(transform: Binding<AffineTransform3D>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./manipulable%28transform,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Applies the given 3D affine transform to the view and allows it to be manipulated using common hand gestures.
- [func manipulationGesture(updating: Binding<Manipulable.GestureState>, coordinateSpace: some CoordinateSpaceProtocol, operations: Manipulable.Operation.Set, inertia: Manipulable.Inertia, isEnabled: Bool, onChanged: ((Manipulable.Event) -> Void)?) -> some View](./manipulationgesture%28updating,coordinatespace,operations,inertia,isenabled,onchanged%29.md)
  Adds a manipulation gesture to this view without allowing this view to be manipulable itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/manipulable(using:))*