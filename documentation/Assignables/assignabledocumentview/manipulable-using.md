# manipulable(using:)

**Framework**: Assignables  
**Kind**: method

Allows the view to be manipulated using a manipulation gesture attached to a different view.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func manipulable(using gestureState: Manipulable.GestureState) -> some View
```

#### Return Value

A view that can be manipulated by a manipulation gesture attached to a different view.

#### Discussion

Use this view modifier alongside `View/manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)` when you want to allow a person to manipulate a view by interacting with a different view.

In the following example, a person can begin a manipulation gesture attached to a deck of cards which, in turn, manipulates a single card instead of the entire deck:

```None
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

> **Note**: `View/manipulationGesture(updating:coordinateSpace:operations:inertia:isEnabled:onChanged:)`

## Parameters

- `gestureState`: The manipulation gesture state that’s updated by a   manipulation gesture added to a different view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/manipulable(using:))*